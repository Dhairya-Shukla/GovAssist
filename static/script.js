// =========================
// SCROLL REVEAL ANIMATION
// =========================

const observer = new IntersectionObserver(entries => {

    entries.forEach(entry => {

        if(entry.isIntersecting){

            entry.target.classList.add('show-card');

        }

    });

});

document.querySelectorAll('.hidden-card').forEach(card => {

    observer.observe(card);

});


// =========================
// HERO TEXT ROTATION
// =========================

const heroTitle = document.getElementById("hero-title");

if(heroTitle){

    const texts = [
        "Find Government Schemes ",
        "Find Scholarships ",
        "Find Farmer Benefits ",
        "Find Employment Schemes "
    ];

    let index = 0;

    setInterval(() => {

        index = (index + 1) % texts.length;

        heroTitle.innerText = texts[index];

    }, 2500);

}


// =========================
// COUNTER ANIMATION
// =========================

const counters = document.querySelectorAll('.counter');

counters.forEach(counter => {

    const updateCounter = () => {

        const target = +counter.getAttribute('data-target');
        const current = +counter.innerText;

        const increment = Math.max(1, Math.ceil(target / 50));

        if(current < target){

            counter.innerText = Math.min(
                current + increment,
                target
            );

            setTimeout(updateCounter, 30);

        } else {

            counter.innerText = target;

        }

    };

    updateCounter();

});


const searchInput = document.getElementById("searchInput");

if(searchInput){

    searchInput.addEventListener("keyup", function(){

        let value = this.value.toLowerCase();

        document.querySelectorAll(".scheme-item").forEach(card => {

            let text = card.innerText.toLowerCase();

            if(text.includes(value)){
                card.style.display = "";
            }else{
                card.style.display = "none";
            }

        });

    });

}