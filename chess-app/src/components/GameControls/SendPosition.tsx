import { useState } from "react";

interface Prop {
  setPosition: Function;
}

function ChangePosition({ setPosition }: Prop) {
  const [inputValue, setInputValue] = useState("");
  const [hide, setHide] = useState(true);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    setPosition(inputValue);
    setInputValue("");
  };

  const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setInputValue(event.target.value);
  };

  let toggle = () => {
    setHide(!hide);
  };

  return (
    <>
      <button id="show pos" onClick={toggle}>
        Change Position
      </button>
      <form id="Change pos" onSubmit={handleSubmit} hidden={hide}>
        <p>
          <label htmlFor="position">Position:</label>
          <input
            name="position"
            id="position"
            type="text"
            value={inputValue}
            onChange={handleChange}
            placeholder="Enter position..."
          />
        </p>
        <p>
          <label htmlFor="ColorToMove">Color to Move</label>
          <br></br>
          <input type="radio" id="White" name="ColorToMove" defaultChecked />
          <label htmlFor="White">White</label>
          <input type="radio" id="Black" name="ColorToMove" />
          <label htmlFor="Black">Black</label>
        </p>
        <p>
          <label htmlFor="CastleRights">CastleRights</label>
          <p>
            <label htmlFor="WhiteKside">White King side</label>
            <input
              type="checkbox"
              name="CastleRights"
              id="WhiteKside"
              defaultChecked
            />
            <label htmlFor="WhiteQside">White Queen side</label>
            <input
              type="checkbox"
              name="CastleRights"
              id="WhiteQside"
              defaultChecked
            />
            <br />
            <label htmlFor="BlackKside">Black King side</label>
            <input
              type="checkbox"
              name="CastleRights"
              id="BlackKside"
              defaultChecked
            />
            <label htmlFor="BlackQside">Black Queen side</label>
            <input
              type="checkbox"
              name="CastleRights"
              id="BlackQside"
              defaultChecked
            />
          </p>
        </p>
        <p>
          <label htmlFor="Enpassant">Enpassant</label>
          <input type="text" placeholder="Enter Enpassant Square..." />
        </p>
        <p>
          <label htmlFor="halfmoves"># of Half Moves</label>
          <input
            type="number"
            id="halfmoves"
            name="halfmoves"
            defaultValue={0}
          />
        </p>
        <p>
          <label htmlFor="fullmoves"># of Full Moves</label>
          <input
            type="number"
            id="fullmoves"
            name="fullmoves"
            defaultValue={0}
          />
        </p>
        <input type="submit" value="Submit" />
        <input type="reset" value="Reset" />
      </form>
    </>
  );
}

export default ChangePosition;
