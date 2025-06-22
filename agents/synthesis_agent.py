# agents/synthesis_agent.py

def synthesize_summaries(summaries, topic):
    print(f"[synthesis_agent] Synthesizing summaries for topic: {topic}")
    if not summaries:
        return "No summaries available to synthesize."
    
    return f"Combined synthesis for '{topic}':\n" + "\n\n".join(summaries)
