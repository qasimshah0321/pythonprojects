{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPlJjT2SvlHHNdfLfsUlP9b",
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
        "<a href=\"https://colab.research.google.com/github/qasimshah0321/pythonprojects/blob/main/Assignment_7_Daily_Expense_Tracker_Muhammad_Qasim_py.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "3mh-zof3Jffc",
        "outputId": "7d891390-88c3-4fac-9e3b-dcf415a572d3"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "Daily Expense Tracker\n",
            "1. Add Expense\n",
            "2. View All Expenses\n",
            "3. View by Category\n",
            "4. View by Date\n",
            "5. Exit\n",
            "Choose option: 1\n",
            "Enter date (YYYY-MM-DD): 2025-06-13\n",
            "Enter category: Dinner\n",
            "Enter amount: 2000\n",
            "Expense added\n",
            "\n",
            "Daily Expense Tracker\n",
            "1. Add Expense\n",
            "2. View All Expenses\n",
            "3. View by Category\n",
            "4. View by Date\n",
            "5. Exit\n",
            "Choose option: 2\n",
            "\n",
            "All Expenses:\n",
            "\n",
            "Date: 2025-06-13\n",
            "  - Dinner: Rs. 2000\n",
            "\n",
            "Daily Expense Tracker\n",
            "1. Add Expense\n",
            "2. View All Expenses\n",
            "3. View by Category\n",
            "4. View by Date\n",
            "5. Exit\n",
            "Choose option: 3\n",
            "Enter category to search: Dinner\n",
            "Total spent on Dinner: Rs. 2000\n",
            "\n",
            "Daily Expense Tracker\n",
            "1. Add Expense\n",
            "2. View All Expenses\n",
            "3. View by Category\n",
            "4. View by Date\n",
            "5. Exit\n",
            "Choose option: 1\n",
            "Enter date (YYYY-MM-DD): 2025-06-12\n",
            "Enter category: Dinner\n",
            "Enter amount: 3500\n",
            "Expense added\n",
            "\n",
            "Daily Expense Tracker\n",
            "1. Add Expense\n",
            "2. View All Expenses\n",
            "3. View by Category\n",
            "4. View by Date\n",
            "5. Exit\n",
            "Choose option: 3\n",
            "Enter category to search: Dinner\n",
            "Total spent on Dinner: Rs. 5500\n",
            "\n",
            "Daily Expense Tracker\n",
            "1. Add Expense\n",
            "2. View All Expenses\n",
            "3. View by Category\n",
            "4. View by Date\n",
            "5. Exit\n",
            "Choose option: 4\n",
            "Enter date (YYYY-MM-DD): 2025-06-13\n",
            "\n",
            "Expenses on 2025-06-13:\n",
            "  - Dinner: Rs. 2000\n",
            "\n",
            "Daily Expense Tracker\n",
            "1. Add Expense\n",
            "2. View All Expenses\n",
            "3. View by Category\n",
            "4. View by Date\n",
            "5. Exit\n",
            "Choose option: 5\n",
            "Goodbye!\n"
          ]
        }
      ],
      "source": [
        "expenses = {}\n",
        "\n",
        "def add_expense():\n",
        "    date = input(\"Enter date (YYYY-MM-DD): \")\n",
        "    category = input(\"Enter category: \").capitalize()\n",
        "    try:\n",
        "        amount = int(input(\"Enter amount: \"))\n",
        "    except ValueError:\n",
        "        print(\"Invalid amount. Please enter a number.\")\n",
        "        return\n",
        "\n",
        "    if date not in expenses:\n",
        "        expenses[date] = []\n",
        "    expenses[date].append({\"category\": category, \"amount\": amount})\n",
        "    print(\"Expense added\")\n",
        "\n",
        "def view_all_expenses():\n",
        "    if not expenses:\n",
        "        print(\"No expenses recorded yet.\")\n",
        "        return\n",
        "    print(\"\\nAll Expenses:\")\n",
        "    for date, records in expenses.items():\n",
        "        print(f\"\\nDate: {date}\")\n",
        "        for entry in records:\n",
        "            print(f\"  - {entry['category']}: Rs. {entry['amount']}\")\n",
        "\n",
        "def view_by_category():\n",
        "    category = input(\"Enter category to search: \").capitalize()\n",
        "    total = 0\n",
        "    for date in expenses:\n",
        "        for entry in expenses[date]:\n",
        "            if entry[\"category\"] == category:\n",
        "                total += entry[\"amount\"]\n",
        "    print(f\"Total spent on {category}: Rs. {total}\")\n",
        "\n",
        "def view_by_date():\n",
        "    date = input(\"Enter date (YYYY-MM-DD): \")\n",
        "    if date in expenses:\n",
        "        print(f\"\\nExpenses on {date}:\")\n",
        "        for entry in expenses[date]:\n",
        "            print(f\"  - {entry['category']}: Rs. {entry['amount']}\")\n",
        "    else:\n",
        "        print(\"No expenses found for this date.\")\n",
        "\n",
        "# Main loop\n",
        "while True:\n",
        "    print(\"\\nDaily Expense Tracker\")\n",
        "    print(\"1. Add Expense\")\n",
        "    print(\"2. View All Expenses\")\n",
        "    print(\"3. View by Category\")\n",
        "    print(\"4. View by Date\")\n",
        "    print(\"5. Exit\")\n",
        "\n",
        "    choice = input(\"Choose option: \")\n",
        "\n",
        "    if choice == \"1\":\n",
        "        add_expense()\n",
        "    elif choice == \"2\":\n",
        "        view_all_expenses()\n",
        "    elif choice == \"3\":\n",
        "        view_by_category()\n",
        "    elif choice == \"4\":\n",
        "        view_by_date()\n",
        "    elif choice == \"5\":\n",
        "        print(\"Goodbye!\")\n",
        "        break\n",
        "    else:\n",
        "        print(\"Invalid option. Please try again.\")\n"
      ]
    }
  ]
}
