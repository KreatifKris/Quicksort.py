from flask import Flask, render_template, request

app = Flask(__name__)

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

@app.route("/", methods=["GET", "POST"])
def index():
    sorted_array = []
    if request.method == "POST":
        user_input = request.form["angka"]
        try:
            angka_list = list(map(int, user_input.split()))
            sorted_array = quick_sort(angka_list)
        except ValueError:
            sorted_array = ["Input tidak valid! Harap masukkan angka saja."]
    return render_template("index.html", hasil=sorted_array)

if __name__ == "__main__":
    app.run(debug=True)
