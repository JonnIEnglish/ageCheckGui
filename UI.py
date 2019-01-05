import toga
from toga.style.pack import *
import ageCheckGUI
import common_funcs


class Root(toga.App):
    def startup(self):
        self.main_window = toga.MainWindow(title='AgeCheck v1.0', size=(500, 620))

        top_box = toga.Box()
        box = toga.Box()
        button = toga.Button('calculate', on_press=self.calculate,
                             style=Pack(alignment=LEFT, padding_top=20, padding_left=40, padding_right=40))

        # BOX LEFT
        left_box = toga.Box(style=Pack(flex=1, direction=COLUMN, width=150, padding_left=30))
        heading_1 = common_funcs.heading('User 1')
        heading_i_1 = common_funcs.heading('INPUTS')
        # INPUTS
        n_1, self.name_1 = common_funcs.text_input('name', False)
        d_1, self.day_1 = common_funcs.selection('day', common_funcs.day_list())
        m_1, self.month_1 = common_funcs.selection('month', common_funcs.month_list())
        y_1, self.year_1 = common_funcs.selection('year', common_funcs.year_list())
        g_1, self.gender_1 = common_funcs.selection('gender', ['male', 'female'])
        heading_o_1 = common_funcs.heading('OUTPUTS')
        # OUTPUTS
        a_1, self.age_1 = common_funcs.text_input('age', True)
        c_d_1, self.crit_d_1 = common_funcs.text_input('crit age low', True)
        c_u_1, self.crit_u_1 = common_funcs.text_input('crit age high', True)
        mch_1, self.match_1 = common_funcs.text_input('match age', True)

        left_box.add(heading_1)
        left_box.add(heading_i_1)
        left_box.add(n_1)
        left_box.add(d_1)
        left_box.add(m_1)
        left_box.add(y_1)
        left_box.add(g_1)
        left_box.add(heading_o_1)
        left_box.add(a_1)
        left_box.add(c_d_1)
        left_box.add(c_u_1)
        left_box.add(mch_1)

        # BOX RIGHT
        right_box = toga.Box(style=Pack(flex=1, direction=COLUMN, width=150, padding_left=50))
        heading_2 = common_funcs.heading('User 2')
        heading_i_2 = common_funcs.heading('INPUTS')
        # INPUTS
        n_2, self.name_2 = common_funcs.text_input('name', False)
        d_2, self.day_2 = common_funcs.selection('day', common_funcs.day_list())
        m_2, self.month_2 = common_funcs.selection('month', common_funcs.month_list())
        y_2, self.year_2 = common_funcs.selection('year', common_funcs.year_list())
        g_2, self.gender_2 = common_funcs.selection('gender', ['male', 'female'])
        heading_o_2 = common_funcs.heading('OUTPUTS')
        # OUTPUTS
        a_2, self.age_2 = common_funcs.text_input('age', True)
        c_d_2, self.crit_d_2 = common_funcs.text_input('crit age low', True)
        c_u_2, self.crit_u_2 = common_funcs.text_input('crit age high', True)
        mch_2, self.match_2 = common_funcs.text_input('match age', True)

        right_box.add(heading_2)
        right_box.add(heading_i_2)
        right_box.add(n_2)
        right_box.add(d_2)
        right_box.add(m_2)
        right_box.add(y_2)
        right_box.add(g_2)
        right_box.add(heading_o_2)
        right_box.add(a_2)
        right_box.add(c_d_2)
        right_box.add(c_u_2)
        right_box.add(mch_2)

        # BOX BELOW
        box_below = toga.Box(style=Pack(flex=1, direction=COLUMN, width=150, padding_left=130, padding_bottom=0, padding_top=20))
        heading_r = common_funcs.heading('RESULTS')
        safe, self.s = common_funcs.text_input('safe?', True)
        m_date, self.m_d = common_funcs.text_input('match date', True)
        t_to_m_date, self.t_t_m_d = common_funcs.text_input('time until safe', True)

        top_box.add(left_box)
        top_box.add(right_box)

        box_below.add(heading_r)
        box_below.add(safe)
        box_below.add(m_date)
        box_below.add(t_to_m_date)

        box.add(top_box)
        box.add(box_below)
        box.add(button)

        top_box.style.update(direction=ROW)
        box.style.update(direction=COLUMN)

        self.main_window.content = box
        self.main_window.show()

    def calculate(self, widget):
        name_1 = self.name_1.value
        day_1 = int(self.day_1.value)
        month_1 = self.month_1.value
        year_1 = int(self.year_1.value)
        gender_1 = self.gender_1.value
        global p1
        p1 = ageCheckGUI.Person(name_1, day_1, common_funcs.get_month(month_1), year_1, gender_1)

        name_2 = self.name_2.value
        day_2 = int(self.day_2.value)
        month_2 = self.month_2.value
        year_2 = int(self.year_2.value)
        gender_2 = self.gender_2.value
        global p2
        p2 = ageCheckGUI.Person(name_2, day_2, common_funcs.get_month(month_2), year_2, gender_2)

        common_funcs.text_output(self.age_1, ageCheckGUI.year_to_age(p1.age))
        common_funcs.text_output(self.age_2, ageCheckGUI.year_to_age(p2.age))
        common_funcs.text_output(self.crit_d_1, ageCheckGUI.year_to_age(p1.crit_age_below))
        common_funcs.text_output(self.crit_d_2, ageCheckGUI.year_to_age(p2.crit_age_below))
        common_funcs.text_output(self.crit_u_1, ageCheckGUI.year_to_age(p1.crit_age_above))
        common_funcs.text_output(self.crit_u_2, ageCheckGUI.year_to_age(p2.crit_age_above))
        match_age_1, match_age_2 = ageCheckGUI.calc_match_age(p1, p2)
        common_funcs.text_output(self.match_1, ageCheckGUI.year_to_age(match_age_1))
        common_funcs.text_output(self.match_2, ageCheckGUI.year_to_age(match_age_2))
        common_funcs.text_output(self.s, ageCheckGUI.is_match_possible(p1, p2))
        match_date, t_to_m_date = ageCheckGUI.calc_match_date(match_age_1, p1)
        common_funcs.text_output(self.m_d, ageCheckGUI.year_to_date(match_date))
        common_funcs.text_output(self.t_t_m_d, ageCheckGUI.year_to_age(t_to_m_date))


def main():
    return Root('Root', 'org.root')


if __name__ == '__main__':
    main().main_loop()
