import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

print("Loading Dataset...")

df = pd.read_csv(
    "datasets/D_dataset.csv"
)

# Features
X = df.drop(
    "diseases",
    axis=1
)

# Target
y = df["diseases"]

print("Encoding Labels...")

encoder = LabelEncoder()

y_encoded = encoder.fit_transform(y)

print("Splitting Dataset...")

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y_encoded,
    test_size=0.2,
    random_state=42
)

print("Training Model...")

model = RandomForestClassifier(
    n_estimators=100,
    max_depth=15,
    random_state=42,
    n_jobs=-1
)

model.fit(
    X_train,
    y_train
)

print("Checking Accuracy...")

pred = model.predict(
    X_test
)

accuracy = accuracy_score(
    y_test,
    pred
)

print(
    f"Accuracy: {accuracy*100:.2f}%"
)

# Save Files
joblib.dump(
    model,
    "models/disease_model.pkl"
)

joblib.dump(
    encoder,
    "models/label_encoder.pkl"
)

joblib.dump(
    list(X.columns),
    "models/features.pkl"
)

print("✅ Model Trained Successfully")
