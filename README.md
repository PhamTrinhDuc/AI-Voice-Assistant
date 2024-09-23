
<div align="center">

<div> VOICE ASSISTANT </div>

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
