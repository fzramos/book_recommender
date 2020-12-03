// globals


// Search page functions
const bookInfoHelper = async () => {
    let search_text = document.getElementById('search-input').value;
    alert(`The form was submitted with the value: ${search_text}`);

    // will get this 
    const rawResults = await getBooksInfo(search_text)
    if (rawResults.totalItems == 0) {
        // TODO make this show message to user saying try again
        console.log('No results')
    } else {
        rawResults.items.forEach(i => {
            console.log(i.volumeInfo.title)
        })
    }
    
    console.log(rawResults)

    

}

async function getBooksInfo(book) {
    // TODO set max to more
    const response = await fetch(`https://www.googleapis.com/books/v1/volumes?q=${book}&maxResults=1`);
    const data = await response.json();
    return data;
}

const searchGenre = () => {
    document.getElementById('search-input').value = 'subject:' + document.getElementById('search-input').value;
    document.getElementById('search-input').focus();

}