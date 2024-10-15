from kivy.uix.boxlayout import BoxLayout

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.properties import StringProperty, ListProperty
from kivymd.uix.list import MDList, OneLineIconListItem
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.label import MDLabel
from kivy.uix.recycleview import RecycleView
from kivy.uix.behaviors import FocusBehavior
from kivymd.uix.pickers import MDDatePicker
from kivymd.uix.datatables import MDDataTable

from kivy.graphics import Color, Rectangle, Line, Ellipse
from kivy.metrics import dp

import datetime
import calendar
from random import random as r


from kivymd.font_definitions import fonts
from kivymd.icon_definitions import md_icons

from kivy.clock import Clock
KV = '''
# https://stackoverflow.com/questions/65698145/kivymd-tab-name-containing-icons-and-text
# this import will prevent disappear tabs through some clicks on them)))
#:import md_icons kivymd.icon_definitions.md_icons
#:import fonts kivymd.font_definitions.fonts



<ItemDrawer>:
    theme_text_color: "Custom"
    on_release: self.parent.set_color_item(self)

    IconLeftWidget:
        id: icon
        icon: root.icon
        theme_text_color: "Custom"
        text_color: root.text_color
        
<ContentNavigationDrawer>:
    orientation: "vertical"
    padding: "8dp"
    spacing: "8dp"

    AnchorLayout:
        anchor_x: "left"
        size_hint_y: None
        height: avatar.height

        Image:
            id: avatar
            size_hint: None, None
            size: "56dp", "56dp"
            source: "kivymd_logo.png"

    MDLabel:
        text: app.title
        font_style: "Button"
        size_hint_y: None
        height: self.texture_size[1]

    MDLabel:
        text: app.by_who
        font_style: "Caption"
        size_hint_y: None
        height: self.texture_size[1]
   
    ScrollView:
        DrawerList:
            id: md_list
Screen:

    MDNavigationLayout:

        ScreenManager:

            Screen:

                BoxLayout:
                    orientation: 'vertical'

                    MDTopAppBar:
                        title: app.title
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.set_state('open')]]
                        right_action_items: [["star-outline", lambda x: app.on_star_click()]]
                        md_bg_color: 0, 0, 0, 1

                    MDTabs:
                        id: tabs
                        on_tab_switch: app.on_tab_switch(*args)
                        height: "48dp"
                        tab_indicator_anim: False
                        background_color: 0.1, 0.1, 0.1, 1
                    
                        Tab:
                            id: tab1
                            name: 'tab1'
                            title: f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['calculator-variant']}[/size][/font] Input"#+tr._('Input')
                            
                            BoxLayout:
                                orientation: 'vertical'
                                padding: "10dp"

                                BoxLayout:
                                    orientation: 'horizontal'

                                    MDIconButton:
                                        icon: "calendar-month"
                                        on_release: app.calc_table() ######################3

                                    MDTextField:
                                        id: start_date
                                        #hint_text: tr._('Start date')
                                        on_focus: if self.focus: app.date_dialog.open()
                                        color_mode: 'custom'
                                        line_color_focus: 0,0,0,1
                                        text_color: 0,0,0,1
                                        current_hint_text_color: 0,0,0,1
                                        ext_hint_color: 0,0,1,1

                                BoxLayout:
                                    orientation: 'horizontal'

                                    MDIconButton:
                                        icon: "cash" 
                                        on_release: app.share_it() ##################3

                                    MDTextField:
                                        id: loan
                                        name: 'loan'
                                        #hint_text: tr._('Loan')
                                        color_mode: 'custom'
                                        line_color_focus: 0,0,0,1
                                        text_color: 0,0,0,1
                                        current_hint_text_color: 0,0,0,1
                                        input_filter: 'float'
                                        helper_text_mode: "on_focus"

                                BoxLayout:
                                    orientation: 'horizontal'

                                    MDIconButton:
                                        icon: "clock-time-five-outline"

                                    MDTextField:
                                        id: months
                                        name: 'months'
                                        #hint_text: tr._('Months')
                                        color_mode: 'custom'
                                        line_color_focus: 0,0,0,1
                                        text_color: 0,0,0,1
                                        current_hint_text_color: 0,0,0,1
                                        input_filter: 'int'
                                        helper_text_mode: "on_focus"


                                BoxLayout:
                                    orientation: 'horizontal'

                                    MDIconButton:
                                        icon: "bank"

                                    MDTextField:
                                        id: interest
                                        name: 'interest'
                                        #hint_text: tr._('Interest')+", %"
                                        color_mode: 'custom'
                                        line_color_focus: 0,0,0,1
                                        text_color: 0,0,0,1
                                        current_hint_text_color: 0,0,0,1
                                        input_filter: 'float'
                                        helper_text_mode: "on_focus"

                                    MDTextField:
                                        id: payment_type
                                        name: 'payment_type'
                                        #hint_text: tr._('Payment type')
                                        text: "annuity"
                                        on_focus:  if self.focus: app.menu.open()
                                        color_mode: 'custom'
                                        line_color_focus: 0,0,0,1
                                        text_color: 0,0,0,1
                                        current_hint_text_color: 0,0,0,1


                                BoxLayout:
                                    orientation: 'horizontal'
                                    padding: "10dp"

                                    MDLabel:
                                        text:'Monthly payment'

                                    MDTextField:
                                        id: payment_label
                                        hint_text: ""
                                        disabled: True

                                BoxLayout:
                                    orientation: 'horizontal'
                                    padding: "10dp"

                                    MDLabel:
                                        text: 'Total interest'

                                    MDTextField:
                                        id: overpayment_loan_label
                                        hint_text: ""
                                        disabled: True

                                BoxLayout:
                                    orientation: 'horizontal'
                                    padding: "10dp"

                                    MDLabel:
                                        text: 'Total payments'

                                    MDTextField:
                                        id: total_amount_of_payments_label
                                        hint_text: ""
                                        disabled: True

                                BoxLayout:
                                    orientation: 'horizontal'
                                    padding: "10dp"

                                    MDLabel:
                                        text: 'Effective'+" %"

                                    MDTextField:
                                        id: effective_interest_rate_label
                                        hint_text: ""
                                        disabled: True
                                        text_hint_color:[0,0,1,1]
                        Tab:

                            id: tab2
                            name: 'tab2'
                            title: f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['table-large']}[/size][/font] Table"#+tr._('Table')
                            
                            
                            ScrollView:
                                MDBoxLayout:
                                    orientation: 'vertical'
                                    id: calc_data_table
                            
                            MDFloatingActionButton:
                                icon: 'email-outline'
                                pos: 20, 20
                                on_release: app.show_confirmation_dialog()

                                    
                        Tab:
                            id: tab3
                            name: 'tab3'
                            title: f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['chart-areaspline']}[/size][/font] Graph"#+tr._('Graph')
                            MDBoxLayout:
                                orientation: 'vertical'
                                padding: '10dp'
                                MDBoxLayout:
                                    orientation: 'vertical'
                                    padding: '10dp'
                                    size_hint_x: 1
                                    size_hint_y: None
                                    height: 50
                                    canvas:
                                        Color:
                                            rgba: 0.2, 0.2, 0.2, 0.1
                                        Rectangle:
                                            size: self.size
                                            pos: self.pos
                                    MDLabel:
                                        text: 'Payment'
                                        halign: 'center'
                                        font_style: 'H5'
                                        height: '48dp'
                            
                                MDBoxLayout:
                                    orientation: 'vertical'
                                    padding: '10dp'
                                    id: graph
                                    canvas:
                                        Color:
                                            rgba: 1, 1, 1, 1
                                        Rectangle:
                                            size: self.size
                                            pos: self.pos
                                MDBoxLayout:
                                    orientation: 'horizontal'
                                    padding: '10dp'
                                    size_hint_x: 1
                                    size_hint_y: None
                                    height: 50
                                    MDIcon:
                                        icon:'checkbox-blank'
                                        halign: 'right'
                                        color: 0, 0, 1, 1
                                        
                                    MDLabel:
                                        text: 'Interest'
                                        halign: 'left'
                                        font_style: 'H6'
                                        height: '48dp'
                                    
                                    MDIcon:
                                        icon:'checkbox-blank'
                                        halign: 'right'
                                        color: 1, 0, 0, 1
                                        
                                    MDLabel:
                                        text: 'Principal'
                                        halign: 'left'
                                        font_style: 'H6'
                                        height: '48dp'
                            
                        Tab:
                            id: tab4
                            name: 'tab4'
                            title: f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['chart-pie']}[/size][/font] Chart"#+tr._('Chart')=
                            MDBoxLayout:
                                orientation: 'vertical'
                                padding: '10dp'
                                MDBoxLayout:
                                    orientation: 'vertical'
                                    padding: '10dp'
                                    size_hint_x: 1
                                    size_hint_y: None
                                    canvas:
                                        Color:
                                            rgba: 0.2, 0.2, 0.2, 0.1
                                        Rectangle:
                                            size: self.size
                                            pos: self.pos
                                    MDLabel:
                                        text: 'Total payment'
                                        halign: 'center'
                                        font_style: 'H5'
                                        height: '48dp'
                                MDBoxLayout:
                                    orientation: 'vertical'
                                    padding: '10dp'
                                    id: chart
                                    canvas:
                                        Color:
                                            rgba: 1, 1, 1, 0.6
                                        Rectangle:
                                            size: self.size
                                            pos: self.pos
                                MDBoxLayout:
                                    orientation: 'horizontal'
                                    padding: '10dp'
                                    size_hint_x: 1
                                    size_hint_y: None
                                    height: 50
                                    MDIcon:
                                        icon:'checkbox-blank'
                                        halign: 'right'
                                        color: 0, 0, 1, 1
                                        
                                    MDLabel:
                                        text: 'Interest'
                                        halign: 'left'
                                        font_style: 'H6'
                                        height: '48dp'
                                    
                                    MDIcon:
                                        icon:'checkbox-blank'
                                        halign: 'right'
                                        color: 1, 0, 0, 1
                                        
                                    MDLabel:
                                        text: 'Principal'
                                        halign: 'left'
                                        font_style: 'H6'
                                        height: '48dp'
                        Tab:
                            id: tab5
                            name: 'tab5'
                            title: f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['book-open-variant']}[/size][/font] Sum"#+tr._('Sum')
                            
                            BoxLayout:
                                orientation: 'vertical'
                                padding: "10dp"

                                BoxLayout:
                                    orientation: 'horizontal'
                                    padding: "10dp"
                                    spacing: "10dp"

                                    MDLabel:
                                        text: 'Property value'
                                        halign: "right"
                                        bold: True

                                    MDLabel:
                                        id: sum_property_value_label
                                        halign: "left"

                                    MDLabel:
                                        text: 'Monthly payment'
                                        halign: "right"
                                        bold: True

                                    MDLabel:
                                        id: sum_payment_label
                                        halign: "left"

                                BoxLayout:
                                    orientation: 'horizontal'
                                    padding: "10dp"
                                    spacing: "10dp"

                                    MDLabel:
                                        text: 'Interest'
                                        halign: "right"
                                        bold: True

                                    MDLabel:
                                        id: sum_interest_label
                                        halign: "left"

                                    MDLabel:
                                        text: 'Total interest'
                                        halign: "right"
                                        bold: True

                                    MDLabel:
                                        id: sum_overpayment_loan_label
                                        halign: "left"

                                BoxLayout:
                                    orientation: 'horizontal'
                                    padding: "10dp"
                                    spacing: "10dp"

                                    MDLabel:
                                        text: 'Start date'
                                        halign: "right"
                                        bold: True

                                    MDLabel:
                                        id: sum_start_date_label
                                        halign: "left"

                                    MDLabel:
                                        text: 'Payments type'
                                        halign: "right"
                                        bold: True

                                    MDLabel:
                                        id: sum_payments_type_label
                                        halign: "left"

                                BoxLayout:
                                    orientation: 'horizontal'
                                    padding: "10dp"
                                    spacing: "10dp"

                                    MDLabel:
                                        text: 'End date'
                                        halign: "right"
                                        bold: True

                                    MDLabel:
                                        id: sum_end_date_label
                                        halign: "left"

                                    MDLabel:
                                        text: 'Effective'+" %"
                                        halign: "right"
                                        bold: True

                                    MDLabel:
                                        id: sum_effective_interest_rate_label
                                        halign: "left"

                                BoxLayout:
                                    orientation: 'horizontal'
                                    padding: "10dp"
                                    spacing: "10dp"

                                    MDLabel:
                                        text: 'Total payments'
                                        halign: "right"
                                        bold: True

                                    MDLabel:
                                        id: sum_total_amount_of_payments_label
                                        halign: "left"

                                    MDLabel:
                                        text: 'Term length'
                                        halign: "right"
                                        bold: True

                                    MDLabel:
                                        id: sum_term_length_label
                                        halign: "left"


        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                id: content_drawer
<ItemTable>:
    size_hint_y: None
    height: '42dp'
    canvas:
        Color:
            rgba: root.color
        Rectangle:
            size: self.size
            pos: self.pos
    MDLabel:
        text: root.num
        halign: 'center'
    MDLabel:
        text: root.date
        halign: 'center'
    MDLabel:
        text: root.payment
        halign: 'center'
    MDLabel:
        text: root.interest
        halign: 'center'
    MDLabel:
        text: root.principal
        halign: 'center'
    MDLabel:
        text: root.debt
        halign: 'center'
            

'''


class ContentNavigationDrawer(BoxLayout):
    pass

class Tab(MDFloatLayout, MDTabsBase):
    pass

class DrawerList(MDList):
    def __init__(self, *args, **kwargs):
        super(DrawerList, self).__init__(*args, **kwargs)


    def set_color_item(self, instance_item):
        '''Called when tap on a menu item.'''
        # Set the color of the icon and text for the menu item.
        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_color


class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()



# https://stackoverflow.com/questions/2249956/how-to-get-the-same-day-of-next-month-of-a-given-day-in-python-using-datetime
def next_month_date(d):
    _year = d.year + (d.month // 12)
    _month = 1 if (d.month // 12) else d.month + 1
    next_month_len = calendar.monthrange(_year, _month)[1]
    next_month = d
    if d.day > next_month_len:
        next_month = next_month.replace(day=next_month_len)
    next_month = next_month.replace(year=_year, month=_month)
    return next_month

# https://kivy.org/doc/stable/examples/gen__canvas__canvas_stress__py.html
def show_canvas_stress(wid):
    with wid.canvas:
        for x in range(10):
            Color(r(), 1, 1, mode='hsv')
            Rectangle(pos=(r() * wid.width + wid.x, r() * wid.height + wid.y), size=(20, 20))

def draw_graph(wid, start_date, loan, months, interest, payment_type):
    # print(wid.x, wid.y)
    with wid.canvas:
        Color(.2, .2, .2, 1)
        Line(rectangle=(wid.x, wid.y, wid.width, wid.height), width=1)
    graph_height = wid.height
    delta_width = wid.width / months

    percent = interest / 100 / 12
    monthly_payment = loan * (percent + percent / ((1 + percent) ** months - 1))

    debt_end_month = loan
    for i in range(0, months):
        repayment_of_interest = debt_end_month * percent
        repayment_of_loan_body = monthly_payment - repayment_of_interest
        debt_end_month = debt_end_month - repayment_of_loan_body
        delta_height_interest = int(repayment_of_interest * graph_height / monthly_payment)
        delta_height_loan = int(repayment_of_loan_body * graph_height / monthly_payment)
        # print("####: ", delta_height_loan, delta_height_loan)
        # print(monthly_payment, repayment_of_interest, repayment_of_loan_body, debt_end_month)
        with wid.canvas:
            Color(1, 0, 0, 1)
            Rectangle(pos=(wid.x + int(i * delta_width), wid.y), size=(int(delta_width), delta_height_loan))
            Color(0, 0, 1, 1)
            Rectangle(pos=(wid.x + int(i * delta_width), wid.y + delta_height_loan),
                      size=(int(delta_width), delta_height_interest))


def draw_chart(wid, total_amount_of_payments, loan):
    interest_chart = ((total_amount_of_payments - loan) * 360) / total_amount_of_payments
    circle_width = wid.width
    center_x = 0
    center_y = wid.height // 2 - circle_width // 2
    if (wid.width > wid.height):
        circle_width = wid.height
        center_x = wid.width // 2 - circle_width // 2
        center_y = 0
    # print(wid.x, wid.y)
    with wid.canvas:
        Color(0, 0, 1, 1)
        Ellipse(pos=(wid.x + center_x, wid.y + center_y), size=(circle_width, circle_width),
                angle_start=360 - int(interest_chart), angle_end=360)
        Color(1, 0, 0, 1)
        Ellipse(pos=(wid.x + center_x, wid.y + center_y), size=(circle_width, circle_width), angle_start=0,
                angle_end=360 - int(interest_chart))
# https://pypi.org/project/kivy-ios/
# https://github.com/kivy/kivy-ios/issues/411
# -----------------
# https://stackoverflow.com/questions/38983649/kivy-android-share-image
# https://stackoverflow.com/questions/63322944/how-to-use-share-button-to-share-content-of-my-app
# Native method for Android.
def share(title, text):
    from kivy import platform

    print(platform)
    if platform == 'android':
        from jnius import autoclass

        PythonActivity = autoclass('org.kivy.android.PythonActivity')
        Intent = autoclass('android.content.Intent')
        String = autoclass('java.lang.String')
        intent = Intent()
        intent.setAction(Intent.ACTION_SEND)
        intent.putExtra(Intent.EXTRA_TEXT, String('{}'.format(text)))
        intent.setType('text/plain')
        chooser = Intent.createChooser(intent, String(title))
        PythonActivity.mActivity.startActivity(chooser)


class MortgageCalculator(MDApp):
    title = 'Mortgage Calculator'
    by_who = "direct_fito@gmail.com"
    menu = None



    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.theme_cls.primary_palette = 'Brown'
        self.theme_cls.primary_hue = 'A100'
        self.screen = Builder.load_string(KV)
        menu_items = [{"icon": "format-text-rotation-angle-up", "text": 'annuity', 'on_release': lambda x=0: self.set_item(x)},
                      {"icon": "format-text-rotation-angle-down", "text": 'differentiated', 'on_release': lambda x=1: self.set_item(x)}]#, 'on_release': self.set_item}]
        self.menu = MDDropdownMenu(
            caller=self.screen.ids.payment_type,
            items=menu_items,
            position='bottom',
            width_mult=4,
        )
        #self.menu.bind(on_release=self.set_item)
        self.date_dialog = MDDatePicker()
        self.date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)

    def set_item(self, ind):#, instance_menu, instance_menu_item):
        print(self.menu, self.menu.items[ind]['text'])
        def set_item(interval):
            print(self.screen.ids.payment_type.text)
            self.screen.ids.payment_type.text = self.menu.items[ind]['text']
            print(self.screen.ids.payment_type.text)
            self.menu.dismiss()
        Clock.schedule_once(set_item, 0.5)

    def on_save(self, instance, value, date_range):
        '''
        Events called when the "OK" dialog box button is clicked.

        :type instance: <kivymd.uix.picker.MDDatePicker object>;

        :param value: selected date;
        :type value: <class 'datetime.date'>;

        :param date_range: list of 'datetime.date' objects in the selected range;
        :type date_range: <class 'list'>;
        '''
        self.get_date(value)
        print(instance, value, date_range)

    def on_cancel(self, instance, value):
        '''Events called when the "CANCEL" dialog box button is clicked.'''
        self.date_dialog.dismiss()
    def get_date(self, date):
        '''
        :type date: <class 'datetime.date'>
        '''
        # pre_start_date = datetime.datetime.strptime(self.screen.ids.start_date.text, "%d-%m-%Y").date()
        print("Before: ", date)#, self.data_for_calc_is_changed, pre_start_date == date)
        self.screen.ids.start_date.text = date.strftime("%d-%m-%Y")  # str(date)
        # if (pre_start_date != date):
        #     self.data_for_calc_is_changed = True
        #print("After: ", date, self.data_for_calc_is_changed, pre_start_date == date)


    def build(self):
        #return Builder.load_string(KV)
        self.theme_cls.theme_style = "Light" # "Dark" # "Light"
        return self.screen

    def on_start(self):
        self.screen.ids.start_date.text = datetime.date.today().strftime("%d-%m-%Y")
        self.screen.ids.loan.text = "50000"
        self.screen.ids.months.text = "12"
        self.screen.ids.interest.text = "22"
        self.screen.ids.payment_type.text = 'annuity'

        icons_item_menu_lines = {
            "account-cowboy-hat": "About author",
            "youtube": "My YouTube",
            "coffee": "Donate author",
            "github": "Source code",
            "share-variant": "Share app",  # air-horn
            "shield-sun": "Dark/Light",
        }
        icons_item_menu_tabs = {
            "calculator-variant": "Input",  # ab-testing
            "table-large": "Table",
            "chart-areaspline": "Graph",
            "chart-pie": "Chart",  # chart-arc
            "book-open-variant": "Sum",
        }
        for icon_name in icons_item_menu_lines.keys():
            self.root.ids.content_drawer.ids.md_list.add_widget(
                ItemDrawer(icon=icon_name, text=icons_item_menu_lines[icon_name])
            )
        # for icon_name, name_tab in icons_item_menu_tabs.items():
        #     self.root.ids.tabs.add_widget(
        #         Tab(title=f"[ref={name_tab}][font={fonts[-1]['fn_regular']}]{md_icons[icon_name]}[/font][/ref]  {name_tab}")
        #         #Tab(title=f'*{name_tab}')
        #     )

    def on_tab_switch(self, instance_tabs, instance_tab, instance_tab_label, tab_text):
        print(instance_tab.ids, instance_tabs,instance_tab_label, tab_text)
        print(tab_text)
    def on_star_click(self):
        # if self.lang == 'en':
        #     self.lang = 'ru'
        # elif self.lang == 'ru':
        #     self.lang = 'en'
        # print(self.current_tab)
        # self.screen.ids.tabs.switch_tab(self.current_tab)
        # self.calc_table(self)
        # self.update_menu()
        pass

    def calc_table(self, *args):
        print("button1 pressed")
        start_date = self.screen.ids.start_date.text
        loan = self.screen.ids.loan.text
        months = self.screen.ids.months.text
        interest = self.screen.ids.interest.text
        payment_type = self.screen.ids.payment_type.text
        print(start_date + " " + loan + " " + months + " " + interest + " " + payment_type)
        # convert to date object, float, and so on
        start_date = datetime.datetime.strptime(self.screen.ids.start_date.text, "%d-%m-%Y").date()
        loan = float(loan)
        months = int(months)
        interest = float(interest)

        row_data_for_tab = []
        # annuity payment
        # https://temabiz.com/finterminy/ap-formula-i-raschet-annuitetnogo-platezha.html
        percent = interest / 100 / 12

        next_date = start_date
        next_prev_date = next_date

        min_monthly_payment = 0
        max_monthly_payment = 0
        monthly_payment = loan * (percent + percent / ((1 + percent) ** months - 1))
        total_amount_of_payments = monthly_payment * months
        overpayment_loan = total_amount_of_payments - loan
        effective_interest_rate = ((total_amount_of_payments / loan - 1) / (months / 12)) * 100
        debt_end_month = loan
        for i in range(0, months):
            repayment_of_interest = debt_end_month * percent
            repayment_of_loan_body = monthly_payment - repayment_of_interest
            debt_end_month = debt_end_month - repayment_of_loan_body
            #print(monthly_payment, repayment_of_interest, repayment_of_loan_body, debt_end_month)
            row_data_for_tab.append(
                [i + 1, next_date.strftime("%d-%m-%Y"), round(monthly_payment, 2), round(repayment_of_interest, 2),
                 round(repayment_of_loan_body, 2), round(debt_end_month, 2)])

        total_amount_of_payments = monthly_payment * months
        overpayment_loan = total_amount_of_payments - loan
        effective_interest_rate = ((total_amount_of_payments / loan - 1) / (months / 12)) * 100
        print(total_amount_of_payments, overpayment_loan, effective_interest_rate)

        debt_end_month = loan
        for i in range(0, months):
            row_color = (0, 0, 0, 1)
            if (i%2!= 0):
                row_color = (0.2, 0.2, 0.2, 0.1)
            repayment_of_interest = debt_end_month * percent
            repayment_of_loan_body = monthly_payment - repayment_of_interest
            debt_end_month = debt_end_month - repayment_of_loan_body

            start_date = next_month_date(start_date)
        #(self.screen.ids.graph)
        show_canvas_stress(self.screen.ids.chart)

        # tab3
        self.screen.ids.graph.canvas.clear()
        draw_graph(self.screen.ids.graph, start_date, loan, months, interest, payment_type)
        # tab4
        self.screen.ids.chart.canvas.clear()
        draw_chart(self.screen.ids.chart, total_amount_of_payments, loan)
        # tab2
        # https://kivymd.readthedocs.io/en/latest/components/datatables/?highlight=datatable
        self.data_tables = MDDataTable(
            use_pagination=True,
            pagination_menu_pos='center',
            rows_num=10,
            # column_data=[
            #     ("№", dp(10)),
            #     (tr._('Date'), dp(20)),
            #     (tr._('Payment'), dp(20)),
            #     (tr._('Interest'), dp(20)),
            #     (tr._('Principal'), dp(20)),
            #     (tr._('Debt'), dp(20)),
            # ],
            column_data=[
                ("№", dp(10)),
                ('Date', dp(20)),
                ('Payment', dp(20)),
                ('Interest', dp(20)),
                ('Principal', dp(20)),
                ('Debt', dp(20)),
            ],
            row_data=row_data_for_tab,
        )
        self.screen.ids.calc_data_table.clear_widgets()
        self.screen.ids.calc_data_table.add_widget(self.data_tables)

        self.screen.ids.payment_label.text = str(round(monthly_payment, 2))
        self.screen.ids.total_amount_of_payments_label.text = str(round(total_amount_of_payments, 2))
        self.screen.ids.overpayment_loan_label.text = str(round(overpayment_loan, 2))
        self.screen.ids.effective_interest_rate_label.text = str(round(effective_interest_rate, 2))

        self.screen.ids.sum_payment_label.text = str(round(monthly_payment, 2))
        self.screen.ids.sum_total_amount_of_payments_label.text = str(round(total_amount_of_payments, 2))
        self.screen.ids.sum_overpayment_loan_label.text = str(round(overpayment_loan, 2))
        self.screen.ids.sum_effective_interest_rate_label.text = str(round(effective_interest_rate, 2))

        self.screen.ids.sum_term_length_label.text = str(round(months, 2)) + " months"
        self.screen.ids.sum_interest_label.text = str(round(interest, 2)) + " %"
        self.screen.ids.sum_property_value_label.text = str(round(loan, 2))

        self.screen.ids.sum_start_date_label.text = start_date.strftime("%d-%m-%Y")
        self.screen.ids.sum_end_date_label.text = next_prev_date.strftime("%d-%m-%Y")

        self.screen.ids.sum_payments_type_label.text = payment_type

        pass

    def show_confirmation_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Share it:",
                type="custom",
                content_cls=ContentDialogSend(),
                buttons=[
                    MDFlatButton(
                        text="CANCEL", text_color=self.theme_cls.primary_color
                    ),
                    MDFlatButton(
                        text="SEND", text_color=self.theme_cls.primary_color
                    ),
                ],
            )
        self.dialog.open()

    def share_it(self, *args):
        share("title_share", "this content to share!")

MortgageCalculator().run()