from app import app
import gc
# gc.disable()
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")