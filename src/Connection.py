import psycopg2

DBNAME = 'db_212'
USER = 'postgres'
PASSWORD = '7280'
HOST = 'localhost'


class DataBase:

    def __init__(self):
        self.connection = psycopg2.connect(dbname=DBNAME, user=USER, password=PASSWORD, host=HOST)
        self.curs = self.connection.cursor()

    def __del__(self):
        self.connection.commit()
        self.curs.close()
        self.connection.close()

    def get_full_table(self):
        self.curs.execute(" select uniq_id, f_value, name_val, otc_val, street_val, bldn, bldn_h, appr, tel \
                from main join families on main.fam=families.f_id join names_ on main.name_=names_.name_id \
                join otchestvo on main.otc=otchestvo.otc_id join streets on main.street=streets.id_street")
        databasejoin = self.curs.fetchall()
        return databasejoin

    def get_families_table(self):
        self.curs.execute("SELECT f_id, f_value FROM families")
        databasefamilies = self.curs.fetchall()
        return databasefamilies

    def get_names_table(self):
        self.curs.execute("SELECT name_id, name_val FROM names_")
        databasenames = self.curs.fetchall()
        return databasenames

    def get_otchestvo_table(self):
        self.curs.execute("SELECT otc_id, otc_val FROM otchestvo")
        databaseotc = self.curs.fetchall()
        return databaseotc

    def get_streets_table(self):
        self.curs.execute("SELECT id_street, street_val FROM streets")
        databasestreets = self.curs.fetchall()
        return databasestreets

    def insert_element_to_main(self, new_element_data):
        # Пример:
        # self.curs.execute("INSERT INTO main VALUES(DEFAULT, 6, 6, 4, 1, '9', '1', 12, '+7(911) 208-56-00')")
        data_message = "INSERT INTO main VALUES(DEFAULT, "
        data = self.get_families_table()
        for rows in data:
            if rows[1] == new_element_data[0]:
                data_message += str(rows[0]) + ", "
                break
        data = self.get_names_table()
        for rows in data:
            if rows[1] == new_element_data[1]:
                data_message += str(rows[0]) + ", "
                break
        data = self.get_otchestvo_table()
        for rows in data:
            if rows[1] == new_element_data[2]:
                data_message += str(rows[0]) + ", "
                break
        data = self.get_streets_table()
        for rows in data:
            if rows[1] == new_element_data[3]:
                data_message += str(rows[0]) + ", "
                break
        if new_element_data[6] == '': new_element_data[6] = 'NULL'
        data_message += "'" + new_element_data[4] + "', '" + \
                        new_element_data[5] + "', " + \
                        new_element_data[6] + ", '" + \
                        new_element_data[7] + "')"
        self.curs.execute(data_message)

    def get_families(self):
        self.curs.execute("SELECT f_value FROM families")
        families = self.curs.fetchall()
        return families

    def get_names(self):
        self.curs.execute("SELECT name_val FROM names_")
        names = self.curs.fetchall()
        return names

    def get_otchestvo(self):
        self.curs.execute("SELECT otc_val FROM otchestvo")
        otc = self.curs.fetchall()
        return otc

    def get_streets(self):
        self.curs.execute("SELECT street_val FROM streets")
        streets = self.curs.fetchall()
        return streets

    def delete_element_from_main(self, uniq_id):
        self.curs.execute("DELETE FROM main WHERE uniq_id = " + uniq_id)

    def element_deletable(self, element):
        database = self.get_full_table()
        for rows in database:
            for items in rows:
                if element == items:
                    return False
        return True

    def delete_element_from_parent_table(self, parent, element_id):
        if parent == 'Фамилии':
            self.curs.execute("DELETE FROM families WHERE f_id = " + element_id)
        elif parent == 'Имена':
            self.curs.execute("DELETE FROM names_ WHERE name_id = " + element_id)
        elif parent == 'Отчества':
            self.curs.execute("DELETE FROM otchestvo WHERE otc_id = " + element_id)
        else:
            self.curs.execute("DELETE FROM streets WHERE id_street = " + element_id)

    def insert_element_to_parent_table(self, parent, element):
        if parent == 'Фамилии':
            self.curs.execute("INSERT INTO families VALUES(DEFAULT, '" + element + "')")
        elif parent == 'Имена':
            self.curs.execute("INSERT INTO names_ VALUES(DEFAULT, '" + element + "')")
        elif parent == 'Отчества':
            self.curs.execute("INSERT INTO otchestvo VALUES(DEFAULT, '" + element + "')")
        else:
            self.curs.execute("INSERT INTO streets VALUES(DEFAULT, '" + element + "')")

    def element_unique(self, parent, element):
        if parent == 'Фамилии':
            data = self.get_families()
        elif parent == 'Имена':
            data = self.get_names()
        elif parent == 'Отчества':
            data = self.get_otchestvo()
        else:
            data = self.get_streets()

        for elements in data:
            if element == elements[0]:
                return False
        return True

    def search_elements_in_main(self, parameters):
        data_message = " SELECT uniq_id, f_value, name_val, otc_val, street_val, bldn, bldn_h, appr, tel \
                FROM main JOIN families ON main.fam=families.f_id JOIN names_ ON main.name_=names_.name_id \
                JOIN otchestvo ON main.otc=otchestvo.otc_id JOIN streets ON main.street=streets.id_street WHERE "
        data_message += "f_value LIKE '%" + parameters[0] + "%' AND "
        data_message += "name_val LIKE '%" + parameters[1] + "%' AND "
        data_message += "otc_val LIKE '%" + parameters[2] + "%' AND "
        data_message += "street_val LIKE '%" + parameters[3] + "%' AND "
        data_message += "bldn LIKE '%" + parameters[4] + "%' AND "
        data_message += "bldn_h LIKE '%" + parameters[5] + "%' AND "
        if parameters[6]:
            data_message += "appr = " + parameters[6] + " AND "
        data_message += "tel LIKE '%" + parameters[7] + "%'"
        self.curs.execute(data_message)
        databasesearch = self.curs.fetchall()
        return databasesearch

    def update_element_in_main(self, uniq_id, elements):
        data_message = "UPDATE main SET bldn = '" + elements[0] + "', bldn_h = '" + elements[1] + "', "
        if elements[2] == "None" or elements[2] == "":
            data_message += "appr = NULL, "
        else:
            data_message += "appr = " + elements[2] + ", "
        data_message += "tel = '" + elements[3] + "' WHERE uniq_id = " + str(uniq_id)
        self.curs.execute(data_message)

    def update_element_in_parent(self, parent, element, element_id):
        data_message = ''
        if parent == 'Фамилии':
            data_message += "UPDATE families SET f_value = '" + element + "' WHERE f_id = " + str(element_id)
        elif parent == 'Имена':
            data_message += "UPDATE names_ SET name_val = '" + element + "' WHERE name_id = " + str(element_id)
        elif parent == 'Отчества':
            data_message += "UPDATE otchestvo SET otc_val = '" + element + "' WHERE otc_id = " + str(element_id)
        else:
            data_message += "UPDATE streets SET street_val = '" + element + "' WHERE id_street = " + str(element_id)
        self.curs.execute(data_message)
