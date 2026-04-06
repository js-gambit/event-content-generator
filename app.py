import streamlit as st
from openai import OpenAI


st.title("Event Content Generator")
st.subheader("Create event marketing copy in seconds")
st.write("Enter the event details below, then click Generate Content.")
st.markdown("""
**Example**
- Event Name: Radiohead
- Genre: Alternative rock
- Location: Stadium
- Audience: Gen X Adults
""")
st.markdown("### Event Details")

event_name = st.text_input("Event Name", placeholder="Radiohead")
genre = st.text_input("Genre", placeholder="Alternative rock")
location = st.selectbox(
    "Location",
    ["Stadium", "Arena", "Theatre", "Outdoor Pavilion", "Club"]
)
audience = st.selectbox(
    "Audience",
    ["Gen Z", "Millennials", "Gen X Adults", "Corporate", "Family", "Luxury"]
)


col1, col2 = st.columns(2)

with col1:
    generate = st.button("Generate Content")

with col2:
    generate_multiple = st.button("Generate 3 Variations")

if generate or generate_multiple:
    if not event_name or not genre or not location or not audience:
        st.warning("Please fill in all fields before generating.")
    else:
        client = OpenAI()
        
        if generate_multiple:
            variation_instruction = "Generate 3 completely different variations of the content."
        else:
            variation_instruction = "Generate 1 strong version."
        prompt = f"""
{variation_instruction}

You are an AI assistant that generates structured event content.

If generating 1 version, return the result in this format:

---
Description:
[write description]

Taglines:
- [tagline 1]
- [tagline 2]
- [tagline 3]

FAQs:
- Q: [question]
  A: [answer]
- Q: [question]
  A: [answer]

If generating 3 variations, return the result in this format:

Version 1:
---
Description:
[write description]

Taglines:
- [tagline 1]
- [tagline 2]
- [tagline 3]

FAQs:
- Q: [question]
  A: [answer]
- Q: [question]
  A: [answer]

Version 2:
---
Description:
[write description]

Taglines:
- [tagline 1]
- [tagline 2]
- [tagline 3]

FAQs:
- Q: [question]
  A: [answer]
- Q: [question]
  A: [answer]

Version 3:
---
Description:
[write description]

Taglines:
- [tagline 1]
- [tagline 2]
- [tagline 3]

FAQs:
- Q: [question]
  A: [answer]
- Q: [question]
  A: [answer]
1. A compelling event description (50–80 words)
2. 3 distinct marketing taglines (under 10 words each)
3. 2 FAQ items attendees might ask

Before generating the final output:
- Identify the core selling angle of the event
- Identify the emotional appeal of the event (e.g., nostalgia, excitement, exclusivity, community)
- Adjust the tone based on the audience and genre

Tone rules:
- Gen Z: energetic, casual, current
- Millennials: polished, engaging, experience-driven
- Gen X Adults: confident, authentic, slightly nostalgic when appropriate
- Corporate: professional and polished
- Luxury: premium and refined
- Family: warm and welcoming

Content rules:
- Make the description vivid and specific to the event type
- Avoid generic phrases like "don't miss out" or "fun for everyone"
- Make each tagline unique in angle and wording
- Make FAQs practical and realistic
- Do not invent overly specific logistics unless provided

Always format your response exactly like this:

Description:
[write description]

Taglines:
- [tagline 1]
- [tagline 2]
- [tagline 3]

FAQs:
- Q: [question]
  A: [answer]
- Q: [question]
  A: [answer]

Event Name: {event_name}
Genre: {genre}
Location: {location}
Audience: {audience}
"""

        try:
            with st.spinner("Generating content..."):
                response = client.responses.create(
                    model="gpt-5.4",
                    input=prompt
                )

            st.text_area("Generated Content", response.output_text, height=500)

        except Exception as e:
            st.error(f"Something went wrong: {e}")