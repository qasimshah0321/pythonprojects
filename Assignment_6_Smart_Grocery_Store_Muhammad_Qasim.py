{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPWnqVCEZsP9fYVjmhdq8px",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/qasimshah0321/pythonprojects/blob/main/Assignment_6_Smart_Grocery_Store_Muhammad_Qasim.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "eD0XqNMIs2fH",
        "outputId": "024a0dc1-7cad-4d4b-e6d6-5671c15650b0"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "Welcome to the Smart Grocery Store Assistant\n",
            "1. View Products\n",
            "2. Add/Update Product\n",
            "3. Purchase Items\n",
            "4. Exit\n",
            "Enter your choice (1-4): 1\n",
            "\n",
            "--- Available Products ---\n",
            "Apple - Rs.100, In stock: 10 \n",
            "Banana - Rs.60, In stock: 20 \n",
            "Milk - Rs.120, In stock: 3 Low Stock!\n",
            "Bread - Rs.80, In stock: 5 \n",
            "\n",
            "\n",
            "Welcome to the Smart Grocery Store Assistant\n",
            "1. View Products\n",
            "2. Add/Update Product\n",
            "3. Purchase Items\n",
            "4. Exit\n",
            "Enter your choice (1-4): 2\n",
            "Enter product name: Coke\n",
            "Enter product price: 200\n",
            "Enter product stock: 10\n",
            "Added new product 'coke' with price Rs.200.0 and stock 10\n",
            "\n",
            "Welcome to the Smart Grocery Store Assistant\n",
            "1. View Products\n",
            "2. Add/Update Product\n",
            "3. Purchase Items\n",
            "4. Exit\n",
            "Enter your choice (1-4): 1\n",
            "\n",
            "--- Available Products ---\n",
            "Apple - Rs.100, In stock: 10 \n",
            "Banana - Rs.60, In stock: 20 \n",
            "Milk - Rs.120, In stock: 3 Low Stock!\n",
            "Bread - Rs.80, In stock: 5 \n",
            "Coke - Rs.200.0, In stock: 10 \n",
            "\n",
            "\n",
            "Welcome to the Smart Grocery Store Assistant\n",
            "1. View Products\n",
            "2. Add/Update Product\n",
            "3. Purchase Items\n",
            "4. Exit\n",
            "Enter your choice (1-4): 4\n",
            "Thank you for using the assistant. Goodbye!\n"
          ]
        }
      ],
      "source": [
        "product_catalog = {\n",
        "    \"apple\": (100, 10),\n",
        "    \"banana\": (60, 20),\n",
        "    \"milk\": (120, 3),\n",
        "    \"bread\": (80, 5)\n",
        "}\n",
        "\n",
        "def display_products():\n",
        "    print(\"\\n--- Available Products ---\")\n",
        "    for product, (price, stock) in product_catalog.items():\n",
        "        alert = \"Low Stock!\" if stock < 5 else \"\"\n",
        "        print(f\"{product.capitalize()} - Rs.{price}, In stock: {stock} {alert}\")\n",
        "    print()\n",
        "\n",
        "def add_or_update_product():\n",
        "    name = input(\"Enter product name: \").lower()\n",
        "    price = float(input(\"Enter product price: \"))\n",
        "    stock = int(input(\"Enter product stock: \"))\n",
        "\n",
        "    if name in product_catalog:\n",
        "        old_price, old_stock = product_catalog[name]\n",
        "        product_catalog[name] = (price, old_stock + stock)\n",
        "        print(f\"Updated '{name}' with price Rs.{price} and stock {old_stock + stock}\")\n",
        "    else:\n",
        "        product_catalog[name] = (price, stock)\n",
        "        print(f\"Added new product '{name}' with price Rs.{price} and stock {stock}\")\n",
        "\n",
        "def purchase_items():\n",
        "    bill = {}\n",
        "    while True:\n",
        "        product = input(\"Enter product to buy (or 'done' to finish): \").lower()\n",
        "        if product == \"done\":\n",
        "            break\n",
        "        if product not in product_catalog:\n",
        "            print(\"Product not found.\")\n",
        "            continue\n",
        "        price, stock = product_catalog[product]\n",
        "        qty = int(input(f\"Enter quantity for {product} (Available: {stock}): \"))\n",
        "\n",
        "        if qty > stock:\n",
        "            print(\"Not enough stock.\")\n",
        "        else:\n",
        "            product_catalog[product] = (price, stock - qty)\n",
        "            if product in bill:\n",
        "                bill[product][1] += qty\n",
        "            else:\n",
        "                bill[product] = [price, qty]\n",
        "            print(f\"Added {qty} x {product} to your cart.\")\n",
        "\n",
        "    if bill:\n",
        "        print(\"\\n --- Purchase Receipt ---\")\n",
        "        total = 0\n",
        "        for product, (price, qty) in bill.items():\n",
        "            subtotal = price * qty\n",
        "            print(f\"{product.capitalize()} - {qty} x Rs.{price} = Rs.{subtotal}\")\n",
        "            total += subtotal\n",
        "        print(f\"Total Bill: Rs.{total}\")\n",
        "    else:\n",
        "        print(\"No items purchased.\")\n",
        "\n",
        "while True:\n",
        "    print(\"\\nWelcome to the Smart Grocery Store Assistant\")\n",
        "    print(\"1. View Products\")\n",
        "    print(\"2. Add/Update Product\")\n",
        "    print(\"3. Purchase Items\")\n",
        "    print(\"4. Exit\")\n",
        "\n",
        "    choice = input(\"Enter your choice (1-4): \")\n",
        "\n",
        "    if choice == \"1\":\n",
        "        display_products()\n",
        "    elif choice == \"2\":\n",
        "        add_or_update_product()\n",
        "    elif choice == \"3\":\n",
        "        purchase_items()\n",
        "    elif choice == \"4\":\n",
        "        print(\"Thank you for using the assistant. Goodbye!\")\n",
        "        break\n",
        "    else:\n",
        "        print(\"Invalid choice. Please enter 1-4.\")\n"
      ]
    }
  ]
}