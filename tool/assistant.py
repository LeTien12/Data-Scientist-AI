from autogen import AssistantAgent , UserProxyAgent
class Engineer:
    def Planner(llm_model):
        planner = AssistantAgent(
            name="Planner",
            system_message='''Plan specific steps to complete the task assigned by the administrator. Only plan, do not write code. 
            State each step in detail without leaving any step out. ''',
            llm_config=llm_model,
        )
        return planner
    
    def Coder(llm_model):
        coder = AssistantAgent(
        name="Coder",
        system_message='''Coder. Writes code to handle the given task.
                        After executing the code, save the code to the appropriate file in the correct directory.
                        Ensure that the file is saved correctly and handle any exceptions if the directory is not accessible.
                        If you want the user to save the code in a file before executing it, put # filename: <filename> inside .Make sure to save the code to disk.
                        ''',
        llm_config=llm_model
    )
        return coder
class User:
    def User(execution_config):
        user_proxy = UserProxyAgent(
        name="Admin",
        system_message="Execute the code if the code has an error then let the coder fix it",
        human_input_mode="TERMINATE",
        code_execution_config=execution_config,
        is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),  
    )
        return user_proxy
    
    