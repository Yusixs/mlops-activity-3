# 1. Library imports
from fastapi import FastAPI, Form
from pydantic import BaseModel
import pickle
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request


# Define the BankNote model for JSON input
class BankNote(BaseModel):
    variance: float
    skewness: float
    curtosis: float
    entropy: float


# 2. Create the app object
app = FastAPI()

# Load the pre-trained classifier
pickle_in = open("classifier.pkl", "rb")
classifier = pickle.load(pickle_in)


# Initialize Jinja2 templates
templates = Jinja2Templates(directory="templates")


# 3. Index route with a styled HTML form
@app.get('/', response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})


# 4. Updated prediction route to handle form data and render result page
@app.post('/predict', response_class=HTMLResponse)
async def predict_banknote(
    request: Request,
    variance: float = Form(...),
    skewness: float = Form(...),
    curtosis: float = Form(...),
    entropy: float = Form(...)
):
    # Prediction using classifier
    prediction = classifier.predict([[variance, skewness, curtosis, entropy]])

    # Interpret the prediction result
    if prediction[0] == 1:
        result = "Fake note"
    else:
        result = "It's a Bank note"

    # Render the result page with the prediction
    return templates.TemplateResponse("result.html", {
                                                        "request": request,
                                                        "prediction": result
                                                    })
