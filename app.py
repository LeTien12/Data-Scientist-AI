import streamlit as st
from tool.assistant import Engineer , User 
from autogen import  GroupChat ,GroupChatManager

llm_config_genmini = {
        "model": "gemini-1.5-flash",
        "api_key": "api_key",
        "api_type": "google",   
        "timeout": 300      
    }

execution_config = { "last_n_messages": 3 ,"work_dir": "save file here", "use_docker": True}

planner = Engineer.Planner(llm_config_genmini)

coder = Engineer.Coder(llm_config_genmini)

user_proxy = User.User()

allowed_transitions = {
    user_proxy: [planner, coder],
    planner: [coder],
    coder: [user_proxy],
}

groupchats = GroupChat(agents=[user_proxy, planner , coder], 
                       allowed_or_disallowed_speaker_transitions=allowed_transitions,
                       speaker_transitions_type="allowed",
                       messages=[], max_round=20, send_introductions=True)

manager = GroupChatManager(groupchat=groupchats, llm_config=llm_config_genmini)

dict_avatar = {
    'Planner' : '👩‍💼',
    'Coder' : '👷‍♀️',
    'Admin' : '🧑‍💻'
}

st.title("Welcome Chatbot AI")



text = st.chat_input("your message")

if text:
    st.spinner("Prosessing .....")
    avatar = '🧑'
    right_aligned_chat_html = f"""
        <div style='display: flex; justify-content: flex-end; align-items: center; margin: 10px 0;'>
            <div style=' padding: 10px; border-radius: 10px; max-width: 60%; margin-right: 10px;'>
                {text}
            </div>
            <div style='flex: none;'>{avatar}</div>
        </div>
        """

    st.markdown(right_aligned_chat_html, unsafe_allow_html=True)

    result = user_proxy.initiate_chat(manager, message= text)
    
    for i in range(2,len(result.chat_history)):
        print(result.chat_history[i])
        chat_message = result.chat_history[i]
        if 'name' in  chat_message:
            name = chat_message["name"]
            with st.chat_message(name, avatar= dict_avatar[name]):
                st.write(name)
                st.code(result.chat_history[i]["content"])




