async function getRoast() {

    const text = document.getElementById("text").value;

    const res = await fetch(`/roast?text=${text}`);

    const data = await res.json();

    document.getElementById("result").innerText =
        data.roast;
}