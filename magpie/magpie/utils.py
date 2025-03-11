import json
import re
from typing import List, Optional, Dict

import pandas as pd


def get_proficiency() -> Dict[int, str]:
    with open("data/proficiency.json", "r", encoding="utf-8") as file:
        proficiency = json.load(file)

    return {int(k): v for k, v in proficiency.items()}


def get_skills() -> Dict[str, str]:
    with open("data/skills.json", "r", encoding="utf-8") as file:
        return json.load(file)


def clean_and_convert_json(
    input_path: str, output_path: Optional[str] = None
) -> List[Dict[str, int]]:
    """
    Args:
        input_path (str): path to raw data
        output_path (Optional[str]): path to output data; if None, data will not be written to a file

    Returns:
        List[Dict[str, int]]: list of dictionaries containing skill and proficiency

    Raises:
        json.JSONDecodeError: if the data is not valid JSON
    """
    # Read the raw file content
    with open(input_path, "r", encoding="utf-8") as file:
        raw_data = file.read()

    # Fix the specific issue: replace colons with commas between key-value pairs
    # This pattern looks for ": "key" :" and replaces it with ": "key", "
    corrected_data = re.sub(r':\s*"([^"]+)"\s*:', r': "\1", ', raw_data)

    try:
        # Try to parse the cleaned data
        parsed_data = json.loads(corrected_data)

        # Sort the data by skill and proficiency
        sorted_data = sorted(parsed_data, key=lambda x: (x["skill"], x["proficiency"]))

        # Write the cleaned data to output file
        if output_path:
            with open(output_path, "w", encoding="utf-8") as file:
                json.dump(sorted_data, file, indent=2)

            print(f"Successfully cleaned and saved to {output_path}")
        return sorted_data

    except json.JSONDecodeError as e:
        print(f"Still having JSON issues: {e}")
        print(f"Error at position {e.pos}: {corrected_data[max(0, e.pos-20):e.pos+20]}")
        raise e


def get_proficiency_by_skill(
    input_path: str, output_path: Optional[str] = None
) -> pd.DataFrame:
    """
    Args:
        input_path (str): path to raw data
        skill (Optional[List[str]]): list of skills to filter by; if None, all skills will be considered
    """
    data = clean_and_convert_json(input_path)

    # these don't appear to be used, but the instructions say to consume the skilsl and proficiency files?
    proficiency = get_proficiency()
    skills = get_skills()

    # aggregating proficiency by skill
    df = pd.DataFrame(data)

    agg = (
        df.groupby("skill")
        .agg(count=("proficiency", "count"), avg_proficiency=("proficiency", "mean"))
        .reset_index()
    )

    agg["avg_proficiency"] = agg["avg_proficiency"].astype(int)

    if output_path:
        # I am also keeping headers in the output file.
        agg.to_csv(output_path, index=False, header=False)
        print(f"Successfully saved to {output_path}")
    return agg
