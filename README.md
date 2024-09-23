
<div align="center">

# VOICE ASSISTANT

</div>

<div align="center">


[![GitHub stars](https://img.shields.io/github/stars/PhamTrinhDuc/AI-Voice-Assistant)](https://github.com/PhamTrinhDuc/AI-Voice-Assistant/stargazers)[![GitHub issues](https://img.shields.io/github/issues/PhamTrinhDuc/CAI-Voice-Assistant)](https://github.com/PhamTrinhDuc/AI-Voice-Assistant/issues)

In this project, I will build a virtual assistant that asks and answers through voice, using Livekit and OpenAI. In addition, I also set a number of separate tasks so that the assistant can respond and adjust according to my wishes.

</div>


## **1. To Install This Application, Follow These Steps:**
#### Step 1. Clone the repository:
```bash
git clone https://github.com/PhamTrinhDuc/AI-Voice-Assistant
cd AI-Voice-Assitant
```
#### Step 2. (Optional) Create and activate a virtual environment:
- For Unix/macOS:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

- For Windows:
```bash
python -m venv venv
.\venv\Scripts\activate
```
- Conda:
```bash
conda create -n <env_name> python=<python_version> 
conda activate env_name
```
#### Step 3. Before starting your application, you need to fill in some evironment variables. Create a `.env` file and fill in these
```bash
OPENAI_API_KEY = "sk-dTKKIChoB9Odh6JlFCbuaKpJVeojvF..."
```

#### Step 4. Install the necessary libraries for the project 
```bash
pip install -r requirements.txt
```
#### Step 5. Run
login to the [Livekit](https://livekit.io/)
```
python3 main.py start
```

## DEMO RESULT
<div align="center">
<img src="./voice assitant.png" alt="demo" width=500 height = 1000/>
</div>
