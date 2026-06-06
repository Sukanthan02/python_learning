"""
Lesson 6.1: Building a ReAct AI Agent from Scratch
--------------------------------------------------
This script builds a fully functional ReAct (Reason + Act) loop in pure Python.
It defines:
1. Agent Tools (Calculator & Mock Stock Price DB)
2. Agent System Prompt (Instructing the LLM how to format thoughts/actions)
3. The ReAct Reasoning Loop (Executing actions, logging observations, and deciding next steps)

Includes a detailed step-by-step execution tracer.
"""

import re

# ==========================================
# 1. Define Agent Tools
# ==========================================

def calculate(expression):
    """Safely evaluates a basic mathematical expression."""
    print(f"   [Tool Call] Executing calculate('{expression}')...")
    # Clean expression to prevent arbitrary code execution
    clean_expr = re.sub(r'[^0-9\+\-\*\/\(\)\. ]', '', expression)
    try:
        return float(eval(clean_expr))
    except Exception as e:
        return f"Error evaluating expression: {e}"

def get_stock_price(ticker):
    """Returns the mock stock price for a given ticker symbol."""
    print(f"   [Tool Call] Executing get_stock_price('{ticker}')...")
    database = {
        "AAPL": 180.00,
        "GOOGL": 150.00,
        "MSFT": 420.00,
        "NVDA": 800.00
    }
    ticker = ticker.upper().strip()
    return database.get(ticker, f"Ticker '{ticker}' not found.")

# List of tools available to the agent
tools = {
    "calculate": calculate,
    "get_stock_price": get_stock_price
}

# ==========================================
# 2. Define the ReAct System Prompt
# ==========================================
SYSTEM_PROMPT = """
You are an AI Agent operating in a loop: Thought, Action, Observation, Thought...
You have access to the following tools:

- get_stock_price: Takes a stock ticker (e.g. AAPL) and returns the current stock price.
- calculate: Takes a math expression (e.g. 10 * 5.2) and returns the result.

Your output format MUST strictly follow this pattern:

Thought: Write down your reasoning process about what to do next.
Action: tool_name(arguments)
Observation: [You will receive this from the system, do not write this yourself]

When you have found the final answer, output:
Final Answer: The final result of the user's request.

Example:
User: What is the price of GOOGL times 2?
Thought: I need to find the price of GOOGL first.
Action: get_stock_price(GOOGL)
Observation: 150.00
Thought: Now I need to multiply 150.00 by 2.
Action: calculate(150.00 * 2)
Observation: 300.00
Thought: I have the final answer.
Final Answer: The price of GOOGL times 2 is 300.00.
"""

# ==========================================
# 3. The ReAct Agent Executor (Simulation Mode)
# ==========================================
class SimulatedReActAgent:
    def __init__(self, query):
        self.query = query
        self.history = []
        
    def step_simulation(self, step_number):
        print(f"\n--- STEP {step_number} ---")
        
        # In a real agent, we send self.query + self.history to the LLM.
        # Below is a hardcoded simulation mapping LLM inputs to outputs
        # to show exactly how the ReAct loop handles responses.
        
        if step_number == 1:
            # Step 1: Agent decides to look up stock price
            print("Thought: I need to find the stock price of AAPL first to answer the user.")
            print("Action: get_stock_price(AAPL)")
            return "Action: get_stock_price(AAPL)"
            
        elif step_number == 2:
            # Step 2: Agent receives stock price, decides to perform calculation
            print("Thought: I see AAPL is priced at 180.00. Now I need to multiply this by 1.25.")
            print("Action: calculate(180.00 * 1.25)")
            return "Action: calculate(180.00 * 1.25)"
            
        elif step_number == 3:
            # Step 3: Agent receives calculation result, states final answer
            print("Thought: The calculation result is 225.0. I have everything required to answer.")
            print("Final Answer: The current stock price of AAPL multiplied by 1.25 is 225.00.")
            return "Final Answer: The current stock price of AAPL multiplied by 1.25 is 225.00."

    def run(self):
        print(f"System Prompt Loaded (Instructs formatting).")
        print(f"User Request: {self.query}")
        
        max_steps = 5
        step = 1
        
        while step <= max_steps:
            # 1. Get Agent Action/Thought (simulated here)
            agent_output = self.step_simulation(step)
            
            # 2. Check if the agent outputted the Final Answer
            if "Final Answer:" in agent_output:
                print("\n=========================================")
                print(f"AGENT SUCCEEDED: {agent_output}")
                print("=========================================")
                break
                
            # 3. Parse action and argument from model output
            action_match = re.search(r'Action:\s*(\w+)\(([^)]+)\)', agent_output)
            if action_match:
                tool_name = action_match.group(1)
                tool_args = action_match.group(2)
                
                # Check if tool exists
                if tool_name in tools:
                    # 4. Execute tool
                    observation = tools[tool_name](tool_args)
                    print(f"Observation: {observation}")
                    
                    # Store observation in history for the next step
                    self.history.append(f"Observation: {observation}")
                else:
                    print(f"Error: Tool '{tool_name}' not found.")
            else:
                print("Error: Could not parse Agent Action. Stopping loop.")
                break
                
            step += 1
            if step > max_steps:
                print("Agent exceeded maximum allowed reasoning steps.")

if __name__ == "__main__":
    # Question that requires multiple tool executions
    query = "What is the stock price of AAPL multiplied by 1.25?"
    agent = SimulatedReActAgent(query)
    agent.run()
