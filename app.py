import streamlit as st
import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth

from services.init import init_state
from components.sidebar import sidebar

from pages.UserHome import user_home

def main():
    init_state()

    with open("config.yaml") as file:
        config = yaml.load(file, Loader=SafeLoader)

    authenticator = stauth.Authenticate(
        config["credentials"],
        config["cookie"]["name"],
        config["cookie"]["key"],
        config["cookie"]["expiry_days"],
        config["preauthorized"],
    )

    # Sidebar
    sidebar(authenticator)

    if (
        st.session_state.choice == "Home"
        and st.session_state.authentication_status
    ):
       user_home()

    elif (
        st.session_state.choice == "Catalog"
        and st.session_state.authentication_status
    ):
        st.write("Catalog")
    elif (
        st.session_state.choice == "Your Orders"
        and st.session_state.authentication_status
    ):
        st.write("Your Orders")

    print(st.session_state.authentication_status)

    # Authentication Pages
    if st.session_state.choice == "Sign in":
        authenticator.login()
        if st.session_state.authentication_status is False:
            st.error("Username/password is incorrect")
        elif st.session_state.authentication_status is None:
            st.warning("Please enter your username and password")
    elif st.session_state.choice == "Sign up":
        try:
            (
                email_of_registered_user,
                _,
                _,
            ) = authenticator.register_user(pre_authorization=False)
            if email_of_registered_user:
                st.success("User registered successfully")
                with open("config.yaml", "w") as file:
                    yaml.dump(config, file, default_flow_style=False)
        except Exception as e:
            st.error(e)


if __name__ == "__main__":
    main()