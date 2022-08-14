function add_item() {
    let items = [];
    let name = document.getElementById("name");
    let origin = document.getElementById("origin");
    let destination = document.getElementById("destination");
    let price = document.getElementById("price");
    let rating = document.getElementById("rating");
    items.push(name);
    items.push(origin);
    items.push(destination);
    items.push(price);
    items.push(rating);
    console.log(items);

    // for(let i=0; i<items.length; i++)
    // {
    //   if(items[i].innerText == "")
    //   {
    //     alert(items[i] + " is empty!");
    //     return;
    //   }
    // }
    //   json_add = { "name" : items[0], "origin" : items[1], "destination" : items[2], "rating" : items[3], "price" : items[4]};
    //   window.flightList.push(json_add);
    console.log(window.flightList);
}