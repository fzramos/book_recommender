


// Search page functions
const getBooks = () => {
    let search_text = document.getElementById('search-input').value;
    alert(`The form was submitted with the value: ${search_text}`);

    fetchResults(search_text)


}

async function fetchResult() {
    let response = await fetch('/readme.txt');
    let data = await response.json();
    console.log(data);
}

const searchGenre = () => {
    document.getElementById('search-input').value = 'subject: ';
    document.getElementById('search-input').focus();

}