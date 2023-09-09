import streamlit as st


def team_members():
    st.write("<h1 style='text-align:center;'>Our Team</h1><br><br>", unsafe_allow_html=True)

    padding_1, main, padding_2 = st.columns((1,2,1))

    with padding_1:
        st.empty()

    with main:
        left, right = st.columns(2)
        
        with left:
            st.image("assets/arpy8.png", width=100)
        with right:
            st.write(f"""
            <h4 style="text-align:center;">Arpit Sengar</h4>
                        
            <table>
                <tr>
                    <th><a href="https://github.com/arpy8">Github</a></th>
                    <th><a href="https://www.linkedin.com/in/arpitsengar">Linkedin</a></th> 
                </tr> 
            </table>
                        
            """, unsafe_allow_html=True)

        st.write("<br><br>", unsafe_allow_html=True)

    with padding_2:
        st.empty()

    # -----

    outer_left, padding, outer_right = st.columns((5,1,5))

    with outer_left:
        left_1, right_1 = st.columns(2)
        
        with left_1:
            st.image("assets/arpy8.png", width=100)
        with right_1:
            st.write(f"""
            <h4 style="text-align:center;">Arpit Sengar</h4>
                        
            <table>
                <tr>
                    <th><a href="https://github.com/arpy8">Github</a></th>
                    <th><a href="https://www.linkedin.com/in/arpitsengar">Linkedin</a></th> 
                </tr> 
            </table>
                        
            """, unsafe_allow_html=True)

        st.write("<br><br>", unsafe_allow_html=True)

        left_2, right_2 = st.columns(2)
        with left_2:
            st.image("assets/arpy8.png", width=100)
        with right_2:
            st.write(f"""
            <h4 style="text-align:center;">Arpit Sengar</h4>
                        
            <table>
                <tr>
                    <th><a href="https://github.com/arpy8">Github</a></th>
                    <th><a href="https://www.linkedin.com/in/arpitsengar">Linkedin</a></th> 
                </tr> 
            </table>
                        
            """, unsafe_allow_html=True)

    with padding:
        st.empty()


    with outer_right:
        left_3, right_3 = st.columns(2)
        
        with left_3:
            st.image("assets/arpy8.png", width=100)
        with right_3:
            st.write(f"""
            <h4 style="text-align:center;">Arpit Sengar</h4>
                    
            <table>
                <tr>
                    <th><a href="https://github.com/arpy8">Github</a></th>
                    <th><a href="https://www.linkedin.com/in/arpitsengar">Linkedin</a></th> 
                </tr> 
            </table>
                        
            """, unsafe_allow_html=True)

        st.write("<br><br>", unsafe_allow_html=True)

        left_4, right_4 = st.columns(2)
        with left_4:
            st.image("assets/arpy8.png", width=100)
        with right_4:
            st.write(f"""
            <h4 style="text-align:center;">Arpit Sengar</h4>
                        
            <table>
                <tr>
                    <th><a href="https://github.com/arpy8">Github</a></th>
                    <th><a href="https://www.linkedin.com/in/arpitsengar">Linkedin</a></th> 
                </tr> 
            </table>
                        
            """, unsafe_allow_html=True)