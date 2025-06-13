{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPWrYAzz9ER+61KlqzlWVtk",
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
        "<a href=\"https://colab.research.google.com/github/qasimshah0321/pythonprojects/blob/main/Python_Crash_Course_Assignment_7_Smart_ATM_Simulator_Muhammad_Qasim_py.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "1rxTU4is03KE",
        "outputId": "d5343525-478c-4670-88a1-82cc60307fd0"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Welcome to ATM\n",
            "Enter account number: 1001\n",
            "Enter PIN: 1234\n",
            "Login successful! Welcome Ali\n",
            "\n",
            "1. View Balance\n",
            "2. Deposit\n",
            "3. Withdraw\n",
            "4. Exit\n",
            "Choose option: 1\n",
            "Current balance: Rs. 5000.0\n",
            "\n",
            "1. View Balance\n",
            "2. Deposit\n",
            "3. Withdraw\n",
            "4. Exit\n",
            "Choose option: 2\n",
            "Enter deposit amount: 2000\n",
            "New balance: Rs. 7000.0\n",
            "\n",
            "1. View Balance\n",
            "2. Deposit\n",
            "3. Withdraw\n",
            "4. Exit\n",
            "Choose option: 3\n",
            "Enter withdrawal amount: 1000\n",
            "Withdrawal successful. New balance: Rs. 6000.0\n",
            "\n",
            "1. View Balance\n",
            "2. Deposit\n",
            "3. Withdraw\n",
            "4. Exit\n",
            "Choose option: 4\n",
            "Session ended. Thank you for using Python ATM.\n"
          ]
        }
      ],
      "source": [
        "accounts = {\n",
        "    1001: {\"name\": \"Ali\", \"pin\": 1234, \"balance\": 5000.0},\n",
        "    1002: {\"name\": \"Sara\", \"pin\": 4321, \"balance\": 8000.0}\n",
        "}\n",
        "\n",
        "def atm_menu(account):\n",
        "    while True:\n",
        "        print(\"\\n1. View Balance\")\n",
        "        print(\"2. Deposit\")\n",
        "        print(\"3. Withdraw\")\n",
        "        print(\"4. Exit\")\n",
        "\n",
        "        choice = input(\"Choose option: \")\n",
        "\n",
        "        if choice == '1':\n",
        "            print(f\"Current balance: Rs. {account['balance']}\")\n",
        "        elif choice == '2':\n",
        "            amount = float(input(\"Enter deposit amount: \"))\n",
        "            account['balance'] += amount\n",
        "            print(f\"New balance: Rs. {account['balance']}\")\n",
        "        elif choice == '3':\n",
        "            amount = float(input(\"Enter withdrawal amount: \"))\n",
        "            if amount <= account['balance']:\n",
        "                account['balance'] -= amount\n",
        "                print(f\"Withdrawal successful. New balance: Rs. {account['balance']}\")\n",
        "            else:\n",
        "                print(\"Insufficient balance!\")\n",
        "        elif choice == '4':\n",
        "            print(\"Session ended. Thank you for using Python ATM.\")\n",
        "            break\n",
        "        else:\n",
        "            print(\"Invalid option. Try again.\")\n",
        "\n",
        "print(\"Welcome to Python ATM\")\n",
        "\n",
        "acc_no = int(input(\"Enter account number: \"))\n",
        "pin = int(input(\"Enter PIN: \"))\n",
        "\n",
        "if acc_no in accounts and accounts[acc_no][\"pin\"] == pin:\n",
        "    print(f\"Login successful! Welcome {accounts[acc_no]['name']}\")\n",
        "    atm_menu(accounts[acc_no])\n",
        "else:\n",
        "    print(\"Invalid account number or PIN.\")\n"
      ]
    }
  ]
}
