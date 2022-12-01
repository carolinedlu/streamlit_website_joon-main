import plotly.graph_objects as go
import calendar
from datetime import datetime
import yaml
from yaml.loader import SafeLoader
import streamlit.components.v1 as components
import os

import streamlit as st  # pip install streamlit
# pip install streamlit_option_menu
from streamlit_option_menu import option_menu
import streamlit_authenticator as stauth  # pip install streamlit_authenticator


st.set_page_config(
    page_title="Centum Joonho",
    page_icon="👋",
    layout="centered",
)


def home(username):
    import streamlit as st
    from streamlit_option_menu import option_menu
    import streamlit_authenticator as stauth  # pip install streamlit_authenticator

    selected = option_menu(menu_title=None, options=["Intro", "Comments", "User"], icons=[
                           "pencil-fill", "bar-chart-fill"], orientation="horizontal",)
    if selected == "Intro":
        st.write("# Welcome to everyone 👋")
        st.sidebar.success("Select selectbox above.")

        st.markdown(
            """
            센텀준호의 홈페이지를 방문해주셔서 감사합니다
            
            해당 페이지는 Streamlit 기반 python 언어로 개발 되었습니다. 
            
            문의 사항은 contact 페이지를 통해 연락 부탁드립니다.

        
            ### Want to learn more?

            - Check out [streamlit.io](https://streamlit.io)
            - Jump into our [documentation](https://docs.streamlit.io)
            - Ask a question in our [communityforums](https://discuss.streamlit.io)
        """
        )

    # navbar -> USer
    if selected == "User":
        st.sidebar.success("Select selectbox above.")

        # Creating an update user details widget
        try:
            if authenticator.update_user_details(username, 'Update user details'):
                st.success('Entries updated successfully')
        except Exception as e:
            st.error(e)

        reset_pw(username)

    if selected == "Comments":
        st.sidebar.success("Select selectbox above.")

        st.subheader('남기고 싶은 말 적어주세요')

        if "my_input" not in st.session_state:
            st.session_state["my_input"] = ""

        my_input = st.text_input(
            "Input a text here", st.session_state["my_input"])
        submit = st.button("입력")

        if submit:
            st.session_state["my_input"] = my_input
            st.write("입력된 내용 : ", my_input)

    # Saving config file
    with open('./config.yaml', 'w') as file:
        yaml.dump(config, file, default_flow_style=False)
# 개발 커리어 화면


def project(username):
    import streamlit as st
    from streamlit_option_menu import option_menu

    # st.set_page_config(
    #     page_title="Project",
    #     page_icon="🌏",
    # )

    st.title("Project")
    st.sidebar.success("Select a page above.")

    selected = option_menu(menu_title=None, options=["Web", "App", "Codes", "Text"], icons=[
                           "pencil-fill", "bar-chart-fill"], orientation="horizontal",)
# 연락


def contact(username):
    import streamlit as st

    # st.set_page_config(
    #     page_title="Contact",
    #     page_icon="📞",
    # )

    st.title("Contact To Me📞")
    st.sidebar.success("Select a page above.")

    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    local_css("style/style.css")

    # contact
    with st.container():
        st.write("---")
        st.header("Get in Touch With Me")
        st.write("##")

        contact_form = """
        <form action="https://formsubmit.co/ghwnsgkgk@kakao.com" method="POST">
        <input type="hidden" name="_captcha" value="false" />
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder ="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
        </form>"""

    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)

    with right_column:
        st.empty()
# 투자


def investment(username):
    import datetime
    import streamlit as st
    import pandas_datareader as pdr  # pip install pandas_datareader
    from cryptocmd import CmcScraper  # pip install cryptocmd
    import plotly.express as px  # pip install plotly-express

    # st.set_page_config(
    #     page_title="Investment Research Data",
    #     page_icon="🤑",
    # )

    st.title("Investment Research Data 🤑")

    st.sidebar.success("Select a page above.")

    # stock
    df = pdr.get_data_yahoo('005930.KS', '2020-01-01', '2022-11-21')

    st.subheader("삼성전자 주식 데이터")
    st.write("마감 가격과 거래량을 차트로 보여줍니다.")
    st.line_chart(df.Close)
    st.line_chart(df.Volume)

    st.subheader('비트코인 BTC 데이터')
    st.write("마감 가격과 거래량을 차트로 보여줍니다.")

    # coin container
    c = st.container()
    name = c.selectbox('Name', ['BTC', 'ETH', 'USDT'])

    start_Date = c.date_input('Start Date', datetime.date(2022, 1, 1))
    end_Date = c.date_input('End Date', datetime.date(2022, 1, 7))

    # coin
    scraper = CmcScraper(name, start_Date.strftime(
        '%d-%m-%Y'), end_Date.strftime('%d-%m-%Y'))

    dd = scraper.get_dataframe()

    fig_close = px.line(
        dd, x='Date', y=['Open', 'High', 'Low', 'Close'], title='가격')
    fig_volume = px.line(dd, x='Date', y=['Volume'], title='Volume')

    st.plotly_chart(fig_close)
    st.plotly_chart(fig_volume)


def saving(username):
    import streamlit as st
    # ------settings--------------------------------
    incomes = ["Salary", "Blog", "Other Income"]

    expenses = ["🏠_Rent", "Utilities", "Groceries",
                "Car", "Other Expenses", "Saving"]

    currency = "KRW"

    page_title = "Income and Expenses Tracker"

    page_icone = ":money_with_wings:"

    layout = "centered"

    # 제일 처음에 위치 해야함
    # st.set_page_config(page_title=page_title,
    #                    page_icon=page_icone, layout=layout)

    st.title(page_title + " " + page_icone)

    st.sidebar.success("Select a page above.")

    # ----------drop down values for selecting the period

    years = [datetime.today().year, datetime.today().year+1]

    months = list(calendar.month_name[1:])

    # ----- naviation menu

    selected = option_menu(menu_title=None, options=["Data Entry", "Data Visualization"], icons=[
        "pencil-fill", "bar-chart-fill"], orientation="horizontal",)

    # -----input & save period
    if selected == "Data Entry":
        st.header(f"Data Entry in {currency}")
        with st.form("entry_from", clear_on_submit=True):
            col1, col2 = st.columns(2)
            col1.selectbox("Select Month : ", months, key="month")
            col2.selectbox("Select Year : ", years, key="year")

            "---"
            with st.expander("Income"):
                for income in incomes:
                    st.number_input(f"{income}:", min_value=0,
                                    format="%i", step=10, key=income)
            with st.expander("Expenses"):
                for expense in expenses:
                    st.number_input(f"{expense}:", min_value=0,
                                    format="%i", step=10, key=expense)
            with st.expander("Comment"):
                comment = st.text_area(
                    "", placeholder="Enter a comment here...")

            "---"
            submitted = st.form_submit_button("Save Data")

            if submitted:
                period = str(st.session_state["year"]) + \
                    "_" + str(st.session_state["month"])
                incomes = {
                    income: st.session_state[income] for income in incomes}
                expenses = {
                    expense: st.session_state[expense] for expense in expenses}
                # TODO : insert vales into database

                st.write(f"income : {incomes}")
                st.write(f"expense : {expenses}")
                st.success("Data Saved")

    # --- PLOT PERIODS
    if selected == "Data Visualization":
        st.header("Data Visualization")
        with st.form("saved_periods"):
            # TODO : get periods from database
            periods = st.selectbox("Select periods :", ["2022_March"])
            submitted = st.form_submit_button("Plot Periods")
            if submitted:
                # TODO : get data from database
                comment = "Some comment"
                incomes = {"Salary": 1500, "Blog": 50, "Other Income": 10}
                expenses = {"🏠_Rent": 600, "Utilities": 200, "Groceries": 300,
                            "Car": 100, "Other Expenses": 50, "Saving": 10}

                # Create metrics
                total_income = sum(incomes.values())
                total_expense = sum(expenses.values())
                remaining_budget = total_income - total_expense
                col1, col2, col3 = st.columns(3)

                col1.metric("Total Income", f"{total_income}{currency}")
                col2.metric("Total Expense", f"{total_expense}{currency}")
                col3.metric("Remaining Budget",
                            f"{remaining_budget}{currency}")

                st.text(f"Comment : {comment}")

                # Create sankey chart

                label = list(incomes.keys()) + \
                    ["Total income"] + list(expenses.keys())
                source = list(range(len(incomes))) + \
                    [len(incomes)]*len(expenses)
                target = [len(incomes)]*len(incomes) + [label.index(expense)
                                                        for expense in expenses]
                value = list(incomes.values()) + list(expenses.values())

                # data to dict dict to sankey

                link = dict(source=source, target=target, value=value)
                node = dict(label=label, pad=20, thickness=30, color="#94ff96")
                data = go.Sankey(link=link, node=node)

                # plot it
                fig = go.Figure(data)
                fig.update_layout(margin=dict(l=0, r=0, t=5, b=5))
                st.plotly_chart(fig, use_container_width=True)


def love(username):
    import streamlit as st

    def intro():
        import streamlit as st

        st.write("# Welcome to Streamlit! 👋")
        st.sidebar.success("Select a demo above.")

        st.markdown(
            """
        """
        )

    def mapping_demo():
        import streamlit as st
        import pandas as pd
        import pydeck as pdk

        from urllib.error import URLError

        st.markdown(f"# {list(page_names_to_funcs.keys())[2]}")
        st.write(
            """
            This demo shows how to use
    [`st.pydeck_chart`](https://docs.streamlit.io/library/api-reference/charts/st.pydeck_chart)
    to display geospatial data.
    """
        )

        @st.cache
        def from_data_file(filename):
            url = (
                "http://raw.githubusercontent.com/streamlit/"
                "example-data/master/hello/v1/%s" % filename
            )
            return pd.read_json(url)

        try:
            ALL_LAYERS = {
                "Bike Rentals": pdk.Layer(
                    "HexagonLayer",
                    data=from_data_file("bike_rental_stats.json"),
                    get_position=["lon", "lat"],
                    radius=200,
                    elevation_scale=4,
                    elevation_range=[0, 1000],
                    extruded=True,
                ),
                "Bart Stop Exits": pdk.Layer(
                    "ScatterplotLayer",
                    data=from_data_file("bart_stop_stats.json"),
                    get_position=["lon", "lat"],
                    get_color=[200, 30, 0, 160],
                    get_radius="[exits]",
                    radius_scale=0.05,
                ),
                "Bart Stop Names": pdk.Layer(
                    "TextLayer",
                    data=from_data_file("bart_stop_stats.json"),
                    get_position=["lon", "lat"],
                    get_text="name",
                    get_color=[0, 0, 0, 200],
                    get_size=15,
                    get_alignment_baseline="'bottom'",
                ),
                "Outbound Flow": pdk.Layer(
                    "ArcLayer",
                    data=from_data_file("bart_path_stats.json"),
                    get_source_position=["lon", "lat"],
                    get_target_position=["lon2", "lat2"],
                    get_source_color=[200, 30, 0, 160],
                    get_target_color=[200, 30, 0, 160],
                    auto_highlight=True,
                    width_scale=0.0001,
                    get_width="outbound",
                    width_min_pixels=3,
                    width_max_pixels=30,
                ),
            }
            st.sidebar.markdown("### Map Layers")
            selected_layers = [
                layer
                for layer_name, layer in ALL_LAYERS.items()
                if st.sidebar.checkbox(layer_name, True)
            ]
            if selected_layers:
                st.pydeck_chart(
                    pdk.Deck(
                        map_style="mapbox://styles/mapbox/light-v9",
                        initial_view_state={
                            "latitude": 37.76,
                            "longitude": -122.4,
                            "zoom": 11,
                            "pitch": 50,
                        },
                        layers=selected_layers,
                    )
                )
            else:
                st.error("Please choose at least one layer above.")
        except URLError as e:
            st.error(
                """
                **This demo requires internet access.**

                Connection error: %s
            """
                % e.reason
            )

    def plotting_demo():
        import streamlit as st
        import time
        import numpy as np

        st.markdown(f'# {list(page_names_to_funcs.keys())[1]}')
        st.write(
            """
            This demo illustrates a combination of plotting and animation with
    Streamlit. We're generating a bunch of random numbers in a loop for around
    5 seconds. Enjoy!
    """
        )

        progress_bar = st.sidebar.progress(0)
        status_text = st.sidebar.empty()
        last_rows = np.random.randn(1, 1)
        chart = st.line_chart(last_rows)

        for i in range(1, 101):
            new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
            status_text.text("%i%% Complete" % i)
            chart.add_rows(new_rows)
            progress_bar.progress(i)
            last_rows = new_rows
            time.sleep(0.05)

        progress_bar.empty()

        # Streamlit widgets automatically run the script from top to bottom. Since
        # this button is not connected to any other logic, it just causes a plain
        # rerun.
        st.button("Re-run")

    def data_frame_demo():
        import streamlit as st
        import pandas as pd
        import altair as alt

        from urllib.error import URLError

        st.markdown(f"# {list(page_names_to_funcs.keys())[3]}")
        st.write(
            """
            This demo shows how to use `st.write` to visualize Pandas DataFrames.

    (Data courtesy of the [UN Data Explorer](http://data.un.org/Explorer.aspx).)
    """
        )

        @st.cache
        def get_UN_data():
            AWS_BUCKET_URL = "http://streamlit-demo-data.s3-us-west-2.amazonaws.com"
            df = pd.read_csv(AWS_BUCKET_URL + "/agri.csv.gz")
            return df.set_index("Region")

        try:
            df = get_UN_data()
            countries = st.multiselect(
                "Choose countries", list(df.index), [
                    "China", "United States of America"]
            )
            if not countries:
                st.error("Please select at least one country.")
            else:
                data = df.loc[countries]
                data /= 1000000.0
                st.write("### Gross Agricultural Production ($B)",
                         data.sort_index())

                data = data.T.reset_index()
                data = pd.melt(data, id_vars=["index"]).rename(
                    columns={"index": "year",
                             "value": "Gross Agricultural Product ($B)"}
                )
                chart = (
                    alt.Chart(data)
                    .mark_area(opacity=0.3)
                    .encode(
                        x="year:T",
                        y=alt.Y("Gross Agricultural Product ($B):Q", stack=None),
                        color="Region:N",
                    )
                )
                st.altair_chart(chart, use_container_width=True)
        except URLError as e:
            st.error(
                """
                **This demo requires internet access.**

                Connection error: %s
            """
                % e.reason
            )

    page_names_to_funcs = {
        "—": intro,
        "Plotting Demo": plotting_demo,
        "Mapping Demo": mapping_demo,
        "DataFrame Demo": data_frame_demo
    }

    demo_name = st.sidebar.selectbox(
        "Choose a demo", page_names_to_funcs.keys())
    page_names_to_funcs[demo_name]()


# ----USE AYTHENTICATION --
cwd = os.getcwd()
st.write(cwd)
with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']

)


def register():
    import yaml
    from yaml.loader import SafeLoader
    import streamlit as st  # pip install streamlit

    try:
        if authenticator.register_user('Register user', 'main', preauthorization=False):
            st.success('User registered successfully')
    except Exception as e:
        st.error(e)

    # Saving config file
    with open('./config.yaml', 'w') as file:
        yaml.dump(config, file, default_flow_style=False)


def forget_username():

    import streamlit as st  # pip install streamlit
    # Creating a forgot username widget
    try:
        username_forgot_username, email_forgot_username = authenticator.forgot_username(
            'Forgot username')
        print(username_forgot_username)
        print(email_forgot_username)
        if username_forgot_username:
            st.success('Your Username : ' + username_forgot_username)

            # Username to be transferred to user securely
        elif username_forgot_username == False:
            st.error('Email not found')
    except Exception as e:
        st.error(e)

    # # Saving config file
    # with open('./config.yaml', 'w') as file:
    #     yaml.dump(config, file, default_flow_style=False)


def forget_pw():
    # Creating a forgot password widget
    try:
        username_forgot_pw, email_forgot_password, random_password = authenticator.forgot_password(
            'Forgot password')
        if username_forgot_pw:
            st.success('New password sent securely')
            # Random password to be transferred to user securely
        elif username_forgot_pw == False:
            st.error('Username not found')
    except Exception as e:
        st.error(e)

    # Saving config file
    # with open('./config.yaml', 'w') as file:
    #     yaml.dump(config, file, default_flow_style=False)


def reset_pw(username):
    # Creating a password reset widget
    try:
        if authenticator.reset_password(username, 'Reset password'):
            st.success('Password modified successfully')
    except Exception as e:
        st.error(e)

    # Saving config file
    with open('./config.yaml', 'w') as file:
        yaml.dump(config, file, default_flow_style=False)


def update_user_d(username):
    # Creating an update user details widget
    try:
        if authenticator.update_user_details(username, 'Update user details'):
            st.success('Entries updated successfully')
    except Exception as e:
        st.error(e)
    # Saving config file
    with open('./config.yaml', 'w') as file:
        yaml.dump(config, file, default_flow_style=False)


def main_login():
    import plotly.graph_objects as go
    import calendar
    from datetime import datetime
    import yaml
    from yaml.loader import SafeLoader
    import streamlit.components.v1 as components

    import streamlit as st  # pip install streamlit
    # pip install streamlit_option_menu
    from streamlit_option_menu import option_menu
    import streamlit_authenticator as stauth  # pip install streamlit_authenticator

    name, authentication_status, username = authenticator.login(
        'Login', 'main')

    # 여기서 부터  home page
    if authentication_status:

        st.write(f'Welcome *{name}*')

        # insert content
        page_names_to_funcs = {
            "🐦HOME": home,
            "🌏PROJECT": project,
            "📞CONTACT": contact,
            "📈INVESTMENT": investment,
            "💰SAVING": saving,
            "🎈LOVE": love

        }
        # sidebar.selectbox

        main_selectbox = st.sidebar.selectbox("목록", page_names_to_funcs.keys())
        page_names_to_funcs[main_selectbox](username)
        authenticator.logout('Logout', 'sidebar')

    elif authentication_status == False:
        st.error('Username/password is incorrect')

    elif authentication_status == None:
        st.warning('Please enter your username and password')


# name, authentication_status, username = authenticator.login('Login', 'main')

authentication_login = {
    "Login🔒": main_login,
    "Sign Up🚀": register,
    "Username lost": forget_username,
    "Password lost": forget_pw
}

authentication_selectbox = st.sidebar.selectbox(
    "Do you have Authenticate?", authentication_login.keys())
authentication_login[authentication_selectbox]()
