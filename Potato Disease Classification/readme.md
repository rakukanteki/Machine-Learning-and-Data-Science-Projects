

# Dataset:
1. Downloaded the dataset from [kaggle](https://www.kaggle.com/datasets/arjuntejaswi/plant-village)
2. Used the datasets of Potatoes.
3. Used Jupyter Notebook and then updated the path of the dataset.

# Training the model:
1. Used `TensorFlow Lite`.

# Backend:
## About FastAPI:
- In-built validation.
- In-built documentation.
- Faster than Python Flask Server.
* Protocols:
> `GET:` Read Data. Ex: Show me a protein jar. <br>
> `POST:` Create the data. Ex: Place the order.<br>
> `PUT:` Update data. Ex: Update the order.<br>
> `DELETE:` Delete an order. Ex: Remove the order.<br>
> `/docs :` Shows the documentation. Useful in analysis. <be>

## About TF Serve:
- Used for deployment of the models while keeping the dame
- `tf serving` makes the model version management and model serving very easy.
- `Batch Inferences`: Can handle many requests easily by grouping them into a batch.

## Using FastAPI:
1. Get into the `api` folder.
```
cd api
```
2. Run the FastAPI server using uvicorn.
```
uvicorn main:app --reload --host 0.0.0.0
```
3. API is now running at `0.0.0.0:8000` port.

## Using FastAPI and TF Serve

# Docker:
## Things to look after:
1. Check WSL installed or not. If not then install
```
wsl --install
```
2. Enable WSL from the Control Panel.
3. Check if virtualization is enabled or not.
