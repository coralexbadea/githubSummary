def split_text_by_length(text, chunk_length):
    text_lines = text.split('\n')
    chunks = []
    current_chunk = ''
    
    for line in text_lines:
        if len(current_chunk) + len(line) <= chunk_length:
            current_chunk += line + '\n'
        else:
            chunks.append(current_chunk)
            current_chunk = line + '\n'
    
    if current_chunk:
        chunks.append(current_chunk)

    return chunks