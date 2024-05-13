import "./Piece.css";

interface Props {
  piece: string;
  keyProp: string; // Add keyProp to the Props interface
  setCurrent: Function;
  setCurrentlocat: Function;
  setPossiblemoves: Function;
}

function Piece({
  piece,
  keyProp,
  setCurrent,
  setCurrentlocat,
  setPossiblemoves,
}: Props) {
  const handleClick = () => {
    showPossible(keyProp); // Pass keyProp to the showPossible function
    setCurrent(piece);
    setCurrentlocat(keyProp);
  };

  const showPossible = (key: string) => {
    let xhr = new XMLHttpRequest();

    xhr.addEventListener("load", () => {
      setPossiblemoves(xhr.responseText.split(","));
    });

    xhr.addEventListener("error", () => {
      console.error("An error occurred while sending the request.");
    });

    let url = "http://127.0.0.1:8000/Functions/Check_moves/" + key;

    xhr.open("GET", url);
    xhr.send();
  };

  return <button className={piece} onClick={handleClick}></button>;
}

export default Piece;
