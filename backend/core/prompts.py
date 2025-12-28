STORY_PROMPT = """
You are a JSON generator.

You MUST return a JSON object that represents a complete choose-your-own-adventure story.
DO NOT return a JSON schema.
DO NOT include "$defs", "properties", "required", or "type".
DO NOT include comments.
DO NOT include markdown.
DO NOT include any text outside JSON.

The JSON MUST follow this structure exactly:

{{
  "title": "Story Title",
  "rootNode": {{
    "content": "The starting situation of the story",
    "isEnding": false,
    "isWinningEnding": false,
    "options": [
      {{
        "text": "Option text",
        "nextNode": {{
          "content": "What happens next",
          "isEnding": false,
          "isWinningEnding": false,
          "options": [
               
               // More nested options
          ]
        }}
      }},

      // More options for root node
    ]
  }}
}}

Rules:
- rootNode must exist
- options must be an array
- Ending nodes MUST have an empty options array
- The story must be 3–4 levels deep
- At least one ending must be a winning ending

Return ONLY valid JSON.
"""
