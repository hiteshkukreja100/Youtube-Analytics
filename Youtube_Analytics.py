{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNO0t8+keiklJ0yqBYoxbqP",
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
        "<a href=\"https://colab.research.google.com/github/hiteshkukreja100/Youtube-Analytics/blob/main/Youtube_Analytics.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "EB10diWFUgm_",
        "outputId": "aaa8edd2-ca83-4620-e467-90d18c1ef09c"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: google-api-python-client in /usr/local/lib/python3.10/dist-packages (2.84.0)\n",
            "Requirement already satisfied: httplib2<1dev,>=0.15.0 in /usr/local/lib/python3.10/dist-packages (from google-api-python-client) (0.22.0)\n",
            "Requirement already satisfied: google-auth<3.0.0dev,>=1.19.0 in /usr/local/lib/python3.10/dist-packages (from google-api-python-client) (2.27.0)\n",
            "Requirement already satisfied: google-auth-httplib2>=0.1.0 in /usr/local/lib/python3.10/dist-packages (from google-api-python-client) (0.1.1)\n",
            "Requirement already satisfied: google-api-core!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.0,<3.0.0dev,>=1.31.5 in /usr/local/lib/python3.10/dist-packages (from google-api-python-client) (2.16.2)\n",
            "Requirement already satisfied: uritemplate<5,>=3.0.1 in /usr/local/lib/python3.10/dist-packages (from google-api-python-client) (4.1.1)\n",
            "Requirement already satisfied: googleapis-common-protos<2.0.dev0,>=1.56.2 in /usr/local/lib/python3.10/dist-packages (from google-api-core!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.0,<3.0.0dev,>=1.31.5->google-api-python-client) (1.63.2)\n",
            "Requirement already satisfied: protobuf!=3.20.0,!=3.20.1,!=4.21.0,!=4.21.1,!=4.21.2,!=4.21.3,!=4.21.4,!=4.21.5,<5.0.0.dev0,>=3.19.5 in /usr/local/lib/python3.10/dist-packages (from google-api-core!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.0,<3.0.0dev,>=1.31.5->google-api-python-client) (3.20.3)\n",
            "Requirement already satisfied: requests<3.0.0.dev0,>=2.18.0 in /usr/local/lib/python3.10/dist-packages (from google-api-core!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.0,<3.0.0dev,>=1.31.5->google-api-python-client) (2.31.0)\n",
            "Requirement already satisfied: cachetools<6.0,>=2.0.0 in /usr/local/lib/python3.10/dist-packages (from google-auth<3.0.0dev,>=1.19.0->google-api-python-client) (5.3.3)\n",
            "Requirement already satisfied: pyasn1-modules>=0.2.1 in /usr/local/lib/python3.10/dist-packages (from google-auth<3.0.0dev,>=1.19.0->google-api-python-client) (0.4.0)\n",
            "Requirement already satisfied: rsa<5,>=3.1.4 in /usr/local/lib/python3.10/dist-packages (from google-auth<3.0.0dev,>=1.19.0->google-api-python-client) (4.9)\n",
            "Requirement already satisfied: pyparsing!=3.0.0,!=3.0.1,!=3.0.2,!=3.0.3,<4,>=2.4.2 in /usr/local/lib/python3.10/dist-packages (from httplib2<1dev,>=0.15.0->google-api-python-client) (3.1.2)\n",
            "Requirement already satisfied: pyasn1<0.7.0,>=0.4.6 in /usr/local/lib/python3.10/dist-packages (from pyasn1-modules>=0.2.1->google-auth<3.0.0dev,>=1.19.0->google-api-python-client) (0.6.0)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from requests<3.0.0.dev0,>=2.18.0->google-api-core!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.0,<3.0.0dev,>=1.31.5->google-api-python-client) (3.3.2)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests<3.0.0.dev0,>=2.18.0->google-api-core!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.0,<3.0.0dev,>=1.31.5->google-api-python-client) (3.7)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests<3.0.0.dev0,>=2.18.0->google-api-core!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.0,<3.0.0dev,>=1.31.5->google-api-python-client) (2.0.7)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests<3.0.0.dev0,>=2.18.0->google-api-core!=2.0.*,!=2.1.*,!=2.2.*,!=2.3.0,<3.0.0dev,>=1.31.5->google-api-python-client) (2024.6.2)\n"
          ]
        }
      ],
      "source": [
        "!pip install google-api-python-client"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from google.colab import userdata\n",
        "key = userdata.get('Google_Cloud')\n"
      ],
      "metadata": {
        "id": "_V00q9qiU0vR"
      },
      "execution_count": 3,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from googleapiclient.discovery import build\n",
        "\n",
        "# Replace with your own API key\n",
        "api_key = key\n",
        "\n",
        "# Create a resource object for interacting with the API\n",
        "youtube = build('youtube', 'v3', developerKey=api_key)\n",
        "\n",
        "def get_latest_videos(channel_id):\n",
        "    # Make a request to the YouTube API to get the latest videos from the channel\n",
        "    request = youtube.search().list(\n",
        "        part=\"snippet\",\n",
        "        channelId=channel_id,\n",
        "        order=\"date\",\n",
        "        maxResults=5  # Number of results to retrieve\n",
        "    )\n",
        "    response = request.execute()\n",
        "\n",
        "    for item in response['items']:\n",
        "        print(f\"Title: {item['snippet']['title']}\")\n",
        "        print(f\"Published At: {item['snippet']['publishedAt']}\")\n",
        "        print(f\"Description: {item['snippet']['description']}\")\n",
        "        print(f\"Video ID: {item['id']['videoId']}\")\n",
        "        print(f\"Video URL: https://www.youtube.com/watch?v={item['id']['videoId']}\")\n",
        "        print(\"\\n\")\n",
        "\n",
        "# Replace with the ID of the YouTube channel you want to get videos from\n",
        "channel_id = \"UC_x5XG1OV2P6uZZ5FSM9Ttw\"  # Example: Google Developers Channel\n",
        "\n",
        "get_latest_videos(channel_id)\n"
      ],
      "metadata": {
        "id": "qwI69_RAVcBM"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}