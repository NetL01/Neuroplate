#: kivy 1.9.1
#: import Toolbar kivymd.toolbar.Toolbar
#: import NoTransition kivy.uix.screenmanager.NoTransition

<StartScreen>:
    orientation: 'vertical'

    Toolbar:
        id: action_bar
        background_color: app.theme_cls.primary_color  # цвет установленной темы
        title: app.title
        opposite_colors: True  # черная либо белая иконка
        elevation: 10  # длинна тени
        # Иконки слева - 
        # left_action_items: [['name-icon', function], …]
        # Иконки справа - 
        # right_action_items: [['name-icon', function], …]

    ScreenManager:
        id: root_manager
        transition: NoTransition() # эффект смены Activity

        Introduction:
            id: introduction
            # Вызывается при выводе текущего Activity на экран.
            on_enter: self._on_enter(action_bar, app)

        CreateAccount:
            id: create_account
            on_enter: self._on_enter(action_bar, app, root_manager)

        AddAccount:
            id: add_account
            on_enter: self._on_enter(action_bar, app)
            # Вызывается при закрытии текущего Activity.
            on_leave: action_bar.title = app.data.string_lang_create_account

        AddAccountOwn:
            id: add_account_own_provider
            on_enter: self._on_enter(action_bar, app, root_manager)
            on_leave: action_bar.title = app.title; action_bar.left_action_items = []
