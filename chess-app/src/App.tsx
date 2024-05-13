import { useState } from "react";
import Board from "./components/Board/Board";
import NewGame from "./components/GameControls/NewGame";
import ChangePosition from "./components/GameControls/SendPosition";
import { useEffect } from "react";

function App() {
  // Add a state to store the position within the entire file
  const [Position, setPosition] = useState(
    "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
  );
  const [Possiblemoves, setPossiblemoves] = useState([""]);
  useEffect(() => {
    loadData(setPosition);
  }, []);

  return (
    <div>
      <h1>Chess</h1>
      <Board
        Position={Position}
        setPosition={setPosition}
        Possiblemoves={Possiblemoves}
        setPossiblemoves={setPossiblemoves}
      />
      <NewGame
        setPosition={setPosition}
        setPossiblemoves={setPossiblemoves}
      ></NewGame>
      <ChangePosition setPosition={setPosition}></ChangePosition>
    </div>
  );
}

export default App;

function loadData(setPosition: Function) {
  let xhr = new XMLHttpRequest();

  xhr.addEventListener("load", () => {
    setPosition(xhr.responseText.split(",")[1].slice(2, -1));
  });

  xhr.addEventListener("error", () => {
    console.error("An error occurred while sending the request.");
  });

  let url = "http://127.0.0.1:8000/Functions/send_board";

  xhr.open("GET", url);
  xhr.send();
}
