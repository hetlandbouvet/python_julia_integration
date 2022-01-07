function stemming_document(document_string)
    
    tokens_data = TokenDocument(document_string)
    stem!(tokens_data)
    stem_tokens_data =  tokens(tokens_data)
    
    return stem_tokens_data
end