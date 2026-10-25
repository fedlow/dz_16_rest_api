from flask import Flask, request, jsonify

app = Flask(__name__)

# --- Наша "база данных" (список словарей) ---
items = [
    {"id": 1, "name": "Ноутбук", "price": 1200},
    {"id": 2, "name": "Мышь", "price": 50}
]

# ==========================================
# 1. GET: Получить все элементы (Без путевого параметра)
# ==========================================
@app.route('/api/items', methods=['GET'])
def get_all_items():
    return jsonify(items), 200

# ==========================================
# 2. GET: Получить один элемент по ID (С путевым параметром <int:item_id>)
# ==========================================
@app.route('/api/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    # Ищем элемент в списке по id
    item = next((i for i in items if i["id"] == item_id), None)
    if item:
        return jsonify(item), 200
    return jsonify({"error": "Элемент не найден"}), 404

# ==========================================
# 3. POST: Создать новый элемент (Без путевого параметра)
# ==========================================
@app.route('/api/items', methods=['POST'])
def create_item():
    data = request.get_json() # Получаем JSON из тела запроса
    
    if not data or "name" not in data:
        return jsonify({"error": "Неверный формат данных. Требуется поле 'name'"}), 400

    # Генерируем новый ID (максимальный существующий + 1)
    new_id = max((i["id"] for i in items), default=0) + 1
    
    new_item = {
        "id": new_id,
        "name": data["name"],
        "price": data.get("price", 0) # Если цена не передана, ставим 0
    }
    items.append(new_item)
    return jsonify(new_item), 201 # 201 Created

# ==========================================
# 4. PUT: Обновить элемент по ID (С путевым параметром <int:item_id>)
# ==========================================
@app.route('/api/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((i for i in items if i["id"] == item_id), None)
    if not item:
        return jsonify({"error": "Элемент не найден"}), 404
        
    data = request.get_json()
    # Обновляем только те поля, которые пришли в запросе
    item["name"] = data.get("name", item["name"])
    item["price"] = data.get("price", item["price"])
    
    return jsonify(item), 200

# ==========================================
# 5. DELETE: Удалить элемент по ID (С путевым параметром <int:item_id>)
# ==========================================
@app.route('/api/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    item = next((i for i in items if i["id"] == item_id), None)
    if not item:
        return jsonify({"error": "Элемент не найден"}), 404
        
    # Оставляем в списке только те элементы, чей id НЕ равен удаляемому
    items = [i for i in items if i["id"] != item_id]
    return jsonify({"message": f"Элемент с id {item_id} удален"}), 200

if __name__ == '__main__':
    app.run(debug=True)