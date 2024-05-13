// acts as an interface between files/components
interface Prop {
  setPosition: Function;
  setPossiblemoves: Function;
}

// Create a function to reset the board to the starting chess position
function StartingPos({ setPosition, setPossiblemoves }: Prop) {
  setPosition("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR");
  setPossiblemoves([""]);

  let xhr = new XMLHttpRequest();

  xhr.addEventListener("error", () => {
    console.error("An error occurred while sending the request.");
  });

  let url = "http://127.0.0.1:8000/Functions/new_board";

  xhr.open("GET", url);
  xhr.send();
}

// Create a function to return a button to call the above function
function NewGame({ setPosition, setPossiblemoves }: Prop) {
  // Returns a button that calls the function
  return (
    <button onClick={() => StartingPos({ setPosition, setPossiblemoves })}>
      New Game
    </button>
  );
}

export default NewGame;
