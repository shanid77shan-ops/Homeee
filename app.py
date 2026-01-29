from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data
CATEGORIES = {
    'kitchen': [
        {'id': 1, 'name': 'Blender', 'price': 50},
        {'id': 2, 'name': 'Toaster', 'price': 30},
    ],
    'bedroom': [
        {'id': 3, 'name': 'Pillow', 'price': 20},
        {'id': 4, 'name': 'Blanket', 'price': 40},
    ]
}
ORDERS = []
USER_PROFILE = {'name': 'John Doe', 'email': 'john@example.com'}

@app.route('/')
def dashboard():
    return render_template('dashboard.html', categories=CATEGORIES)

@app.route('/order/<category>/<int:item_id>', methods=['POST'])
def order_item(category, item_id):
    item = next((i for i in CATEGORIES[category] if i['id'] == item_id), None)
    if item:
        ORDERS.append(item)
    return redirect(url_for('order_list'))

@app.route('/orders')
def order_list():
    return render_template('orders.html', orders=ORDERS)

@app.route('/profile')
def profile():
    return render_template('profile.html', profile=USER_PROFILE)

if __name__ == '__main__':
    app.run(debug=True)
