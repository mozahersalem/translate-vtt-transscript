# VTT Translation Project

This project provides a set of scripts to process, translate, and merge VTT (Web Video Text Tracks) files. The main steps include extracting specific lines from a VTT file, translating those lines using the Google Translate API, and merging the translations back into the original VTT file.

## Table of Contents

- [VTT Translation Project](#vtt-translation-project)
  - [Table of Contents](#table-of-contents)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Usage](#usage)
    - [Step 1: Add your non EN file to `src/files/transcript`](#step-1-add-your-non-en-file-to-srcfilestranscript)

## Prerequisites

- Python 3.x
- Google Cloud Translate API credentials
- Required Python libraries: `python-docx`, `google-cloud-translate`

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/vtt-translation-project.git
    cd vtt-translation-project
    ```

2. Install the required Python libraries:
    ```sh
    ./bootstrap.sh
    ```

3. Set up Google Cloud Translate API credentials:
    - Follow the instructions [here](https://cloud.google.com/translate/docs/setup) to set up your Google Cloud project and obtain the credentials JSON file.
    - Set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to the path of your credentials JSON file:
        ```sh
        export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/credentials.json"
        ```

## Usage

### Step 1: Add your non EN file to `src/files/transcript`

After run main.py `dist` file will be generated with the following files:
 -  Modified_transcript.vtt
    -  All the unnessery lines will be skipped and keep the acuall transaction lines and will be saved to `transcript.docx`
        ```bash
        WEBVTT

        1
        00:00:00.030 --> 00:00:01.180
        Name: Ja.

        2
        00:00:11.780 --> 00:00:12.830
        Name: Eine.

        3
        00:00:14.510 --> 00:00:28.789
        Name: Hier fehlt ein kleines Wort. Das ist kein Artikel. Das ist ein Wort, das wir verwenden, wenn wir Zusätze haben mit der Frage, wofür?

        4
        00:00:29.140 --> 00:00:30.470
        Name: Wofür?

        5
        00:00:32.259 --> 00:00:32.599
        Name: Um.

        6
        00:00:34.730 --> 00:00:35.370
        Name: Oma.

        7
        00:00:35.370 --> 00:00:38.160
        Name: Wofür benutzen wir eine Waschmaschine?

        8
        00:00:38.670 --> 00:00:48.030
        Name: Wir benutzen sie, um schmutzige Kleidung wieder sauber zu machen. Dieser Satz mit um. Der hat kein Subjekt.

        ```

 -  transcript.docx
    -  WIll include the dialog scriopts only, then this file will be translated to the English language using `Google translate API` and save the oyput to `en-transcript.docx`
 -  DE_EN_transcript.vtt
    -  Will contain the the transscript with teh non english language then the English script will be added below.
        ```Bash
        WEBVTT

        1
        00:00:00.030 --> 00:00:01.180
        Name: Ja.
        Name: Yes.

        2
        00:00:11.780 --> 00:00:12.830
        Name: Eine.
        Name: One.

        3
        00:00:14.510 --> 00:00:28.789
        Name: Hier fehlt ein kleines Wort. Das ist kein Artikel. Das ist ein Wort, das wir verwenden, wenn wir Zusätze haben mit der Frage, wofür?
        Name: There is a small word missing here. It is not an article. It is a word we use when we have additions with the question, what for?

        4
        00:00:29.140 --> 00:00:30.470
        Name: Wofür?
        Name: For what?

        5
        00:00:32.259 --> 00:00:32.599
        Name: Um.
        Name: Um.

        6
        00:00:34.730 --> 00:00:35.370
        Name: Oma.
        Name: My own.

        7
        00:00:35.370 --> 00:00:38.160
        Name: Wofür benutzen wir eine Waschmaschine?
        Name: What do we use a washing machine for?

        8
        00:00:38.670 --> 00:00:48.030
        Name: Wir benutzen sie, um schmutzige Kleidung wieder sauber zu machen. Dieser Satz mit um. Der hat kein Subjekt.
        Name: We use them to clean dirty clothes again. This sentence with um. It has no subject.

        ```
