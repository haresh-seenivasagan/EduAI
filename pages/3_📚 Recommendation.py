import requests
import streamlit as st

def get_books(search_term):
    # search for books on Open Library
    response = requests.get(f"https://openlibrary.org/search.json?q={search_term}")

    # extract book data from response
    data = response.json()
    books = []
    for doc in data['docs']:
        title = doc.get('title', '')
        author = ', '.join(doc.get('author_name', []))
        year = doc.get('first_publish_year', None)
        if year is not None:
            year = int(year)
        description = doc.get('description', '')
        books.append((title, author, year, description))

    # recommend top-rated books
    if len(books) > 0:
        recommended_books = sorted([book for book in books if book[2] is not None], key=lambda x: x[2], reverse=True)[:5]
        return recommended_books
    else:
        return None
st.title("Book Recommendation Engine")
search_term = st.text_input("Enter a book title:")
if search_term:
    recommended_books = get_books(search_term)
    if recommended_books:
        st.subheader("Based on your input, we recommend the following books:")
        for i, book in enumerate(recommended_books):
            st.write(f"{i+1}. '{book[0]}' by {book[1]} (published in {book[2]})")
            st.write(book[3])
            st.write("")
    else:
        st.write("No books found.")
