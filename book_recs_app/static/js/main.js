// globals

// <div id="slider"></div>
// var slider = document.getElementById('slider');
// noUiSlider.create(slider, {
//     start: [20, 80],
//     connect: true,
//     range: {
//         'min': 0,
//         'max': 100
//     }
// });

function toggleSurvey() {
    const survey = document.getElementById('survey');
    survey.hidden = (!survey.hidden);
}



// Search page functions
const bookInfoHelper = async () => {

    let search_text = document.getElementById('search-input').value; 

    // reseting book card grid for new results
    const book_cards = document.querySelectorAll('.book-card');
    book_cards.forEach(card => {
        if (!card.hasAttribute("hidden")) {
            card.setAttribute('hidden', 'True');
        }
    })

    
    const rawResults = await getBooksInfo(search_text)
    if (rawResults.totalItems == 0) {
        // TODO make this show message to user saying try again
        console.log('No results')
    } else {
        rawResults.items.forEach(i => {
            // console.log(i.volumeInfo.title)
            // TODO append results to search page with function
            addBookCard(i)
        })
    }
    console.log(rawResults)
}

async function getBooksInfo(book, max = 4) {
    // TODO set max to more
    const response = await fetch(`https://www.googleapis.com/books/v1/volumes?q=${book}&maxResults=${max}`);
    const data = await response.json();
    return data;
}

const searchGenre = () => {
    document.getElementById('search-input').value = 'subject:' + document.getElementById('search-input').value;
    document.getElementById('search-input').focus();

}

const addBookCard = (items) => {
    console.log(items.volumeInfo.title)

    const book_cards = document.querySelectorAll('.book-card');

    for (let i = 0; i < book_cards.length; i++) {
        if (book_cards[i].hasAttribute("hidden")) {
            book_cards[i].removeAttribute('hidden');
            var book_info = book_cards[i].firstElementChild.firstElementChild.childNodes;
            
            if ('title' in items.volumeInfo) {
                book_info[1].innerHTML = items.volumeInfo.title;
            } else {
                book_info[1].innerHTML = 'Unknown Title'
            }

            if ('previewLink' in items.volumeInfo) {
                book_info[3].href = items.volumeInfo.previewLink;
                book_info[9].href = items.volumeInfo.previewLink;
            } else {
                book_info[3].href = alert('Sorry, preview is not working.');
                book_info[9].href = alert('Sorry, preview is not working.');
            }

            if ('imageLinks' in items.volumeInfo) {
                book_info[3].firstElementChild.src = items.volumeInfo.imageLinks.thumbnail;
            } else {
                book_info[3].firstElementChild.src = '../static/images/dark_default_cover_small.jpg';
            }

            if ('authors' in items.volumeInfo) {
                book_info[5].innerHTML = items.volumeInfo.authors[0];
            } else {
                book_info[5].innerHTML = 'Author Unknown'
            }
            
            // book_info[1].innerHTML = items.volumeInfo.title;
            // book_info[3].href = items.volumeInfo.previewLink;
            // book_info[3].firstElementChild.src = items.volumeInfo.imageLinks.thumbnail;
            // book_info[5].innerHTML = items.volumeInfo.authors[0];

            // book_info[9].href = items.volumeInfo.previewLink;
            
            // book_info[2].innerHTML = items.volumeInfo.description;
            // save for later
            break
        }
    }

}

window.addEventListener('load', async (event) => {
    ISBNInfoHelper();
});

async function ISBNInfoHelper() {
    let isbn_obj = document.getElementsByClassName('serial')

    // reseting book card grid for new results
    const book_cards = document.querySelectorAll('.book-card');
    book_cards.forEach(card => {
        if (!card.hasAttribute("hidden")) {
            card.setAttribute('hidden', 'True');
        }
    })

    for (const property in isbn_obj) {
        // isbn_obj[property]
        const rawResults = await getBooksInfo(isbn_obj[property].innerHTML, max=1)
        if (rawResults.totalItems == 0) {
            // TODO make this show message to user saying try again
            console.log('No results')
        } else {
            rawResults.items.forEach(i => {
                // console.log(i.volumeInfo.title)
                addBookCard(i)
            })
        }
    }

    console.log(rawResults)
}
