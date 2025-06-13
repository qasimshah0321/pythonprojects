{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyP/rnjeA/YS/2UaSP8WkWAc",
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
        "<a href=\"https://colab.research.google.com/github/qasimshah0321/pythonprojects/blob/main/Assignment_7_Online_Course_Enrollment_System_Muhammad_Qasim_py.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "7JNkwlF_BK6B",
        "outputId": "1a2bb91f-2913-4752-bfbb-586cf7c8d877"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "Welcome to Online Courses\n",
            "1. View Courses\n",
            "2. Enroll\n",
            "3. Drop\n",
            "4. View Students\n",
            "5. Exit\n",
            "Choose option: 2\n",
            "Enter course name: AI\n",
            "Enter student name: Junaid\n",
            "Junaid enrolled in Ai\n",
            "\n",
            "Welcome to Online Courses\n",
            "1. View Courses\n",
            "2. Enroll\n",
            "3. Drop\n",
            "4. View Students\n",
            "5. Exit\n",
            "Choose option: 2\n",
            "Enter course name: python\n",
            "Enter student name: Kamran\n",
            "Kamran enrolled in Python\n",
            "\n",
            "Welcome to Online Courses\n",
            "1. View Courses\n",
            "2. Enroll\n",
            "3. Drop\n",
            "4. View Students\n",
            "5. Exit\n",
            "Choose option: 4\n",
            "Enter course name to view students: ai\n",
            "Enrolled Students in Ai: ['Junaid']\n",
            "\n",
            "Welcome to Online Courses\n",
            "1. View Courses\n",
            "2. Enroll\n",
            "3. Drop\n",
            "4. View Students\n",
            "5. Exit\n",
            "Choose option: 4\n",
            "Enter course name to view students: Python\n",
            "Enrolled Students in Python: ['Kamran']\n",
            "\n",
            "Welcome to Online Courses\n",
            "1. View Courses\n",
            "2. Enroll\n",
            "3. Drop\n",
            "4. View Students\n",
            "5. Exit\n"
          ]
        }
      ],
      "source": [
        "courses = {\n",
        "    \"python\": {\"seats\": 3, \"students\": []},\n",
        "    \"ai\": {\"seats\": 2, \"students\": []},\n",
        "    \"data science\": {\"seats\": 1, \"students\": []}\n",
        "}\n",
        "\n",
        "def view_courses():\n",
        "    print(\"\\nAvailable Courses:\")\n",
        "    for course, info in courses.items():\n",
        "        print(f\"{course.title()} - Seats Left: {info['seats']}\")\n",
        "\n",
        "def enroll_student():\n",
        "    course_name = input(\"Enter course name: \").strip().lower()\n",
        "    student_name = input(\"Enter student name: \").strip().title()\n",
        "\n",
        "    if course_name not in courses:\n",
        "        print(\"Course not found.\")\n",
        "        return\n",
        "\n",
        "    if courses[course_name][\"seats\"] > 0:\n",
        "        courses[course_name][\"students\"].append(student_name)\n",
        "        courses[course_name][\"seats\"] -= 1\n",
        "        print(f\"{student_name} enrolled in {course_name.title()}\")\n",
        "    else:\n",
        "        print(\"No seats available in this course.\")\n",
        "\n",
        "def drop_course():\n",
        "    course_name = input(\"Enter course name: \").strip().lower()\n",
        "    student_name = input(\"Enter student name to drop: \").strip().title()\n",
        "\n",
        "    if course_name in courses and student_name in courses[course_name][\"students\"]:\n",
        "        courses[course_name][\"students\"].remove(student_name)\n",
        "        courses[course_name][\"seats\"] += 1\n",
        "        print(f\"{student_name} has been removed from {course_name.title()}\")\n",
        "    else:\n",
        "        print(\"Student not enrolled in this course or course doesn't exist.\")\n",
        "\n",
        "def view_students():\n",
        "    course_name = input(\"Enter course name to view students: \").strip().lower()\n",
        "    if course_name in courses:\n",
        "        print(f\"Enrolled Students in {course_name.title()}: {courses[course_name]['students']}\")\n",
        "    else:\n",
        "        print(\"Course not found.\")\n",
        "\n",
        "# Main Menu\n",
        "while True:\n",
        "    print(\"\\nWelcome to Online Courses\")\n",
        "    print(\"1. View Courses\")\n",
        "    print(\"2. Enroll\")\n",
        "    print(\"3. Drop\")\n",
        "    print(\"4. View Students\")\n",
        "    print(\"5. Exit\")\n",
        "\n",
        "    choice = input(\"Choose option: \")\n",
        "\n",
        "    if choice == '1':\n",
        "        view_courses()\n",
        "    elif choice == '2':\n",
        "        enroll_student()\n",
        "    elif choice == '3':\n",
        "        drop_course()\n",
        "    elif choice == '4':\n",
        "        view_students()\n",
        "    elif choice == '5':\n",
        "        print(\"Thank you for using the Course Enrollment System!\")\n",
        "        break\n",
        "    else:\n",
        "        print(\"Invalid option. Please try again.\")\n"
      ]
    }
  ]
}
