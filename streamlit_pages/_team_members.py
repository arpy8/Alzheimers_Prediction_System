from config import TEAM_MEMBERS, EMOJI
import streamlit as st


def team_members():
    st.markdown(f"<h1 style='text-align:center;'>Meet our dedicated team members</h1>", unsafe_allow_html=True)
    st.markdown("<br><br><div class='team-container'>", unsafe_allow_html=True)

    t_left, t_mid, t_right = st.columns(3)

    with t_left:
        st.markdown(
            f"""
            <a href={TEAM_MEMBERS[0]['links'][0]} target="_blank">
                <div class='team-member'>
                    <h3>{TEAM_MEMBERS[0]['name']}</h3>
                    <p>{TEAM_MEMBERS[0]['role']}</p>
                </div>
            </a>
            <br>
            """,
            unsafe_allow_html=True
        )

    with t_mid:
        st.image(EMOJI)
        st.empty()

    with t_right:
        st.markdown(
            f"""
            <a href={TEAM_MEMBERS[1]['links'][0]} target="_blank">
                <div class='team-member'>
                    <h3>{TEAM_MEMBERS[1]['name']}</h3>
                    <p>{TEAM_MEMBERS[1]['role']}</p>
                </div>
            </a>
            <br>
            """,
            unsafe_allow_html=True
        )


    b_left, b_mid, b_right = st.columns(3)

    with b_left:
        st.markdown(
            f"""
            <a href={TEAM_MEMBERS[2]['links'][0]} target="_blank">
                <div class='team-member'>
                    <h3>{TEAM_MEMBERS[2]['name']}</h3>
                    <p>{TEAM_MEMBERS[2]['role']}</p>
                </div>
            </a>
            <br>
            """,
            unsafe_allow_html=True
        )

    with b_mid:
        st.markdown(
            f"""
            <a href={TEAM_MEMBERS[3]['links'][0]} target="_blank">
                <div class='team-member'>
                    <h3>{TEAM_MEMBERS[3]['name']}</h3>
                    <p>{TEAM_MEMBERS[3]['role']}</p>
                </div>
            </a>
            <br>
            """,
            unsafe_allow_html=True
        )

    with b_right:
        st.markdown(
            f"""
            <a href={TEAM_MEMBERS[4]['links'][0]} target="_blank">
                <div class='team-member'>
                    <h3>{TEAM_MEMBERS[4]['name']}</h3>
                    <p>{TEAM_MEMBERS[4]['role']}</p>
                </div>
            </a>
            <br>
            """,
            unsafe_allow_html=True
        )
        