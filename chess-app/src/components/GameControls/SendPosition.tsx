import { useState } from "react";

interface Prop {
  setPosition: Function;
}

function ChangePosition({ setPosition }: Prop) {
  const [inputValue, setInputValue] = useState("");

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    setPosition(inputValue);
    setInputValue("");
  };

  const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setInputValue(event.target.value);
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        value={inputValue}
        onChange={handleChange}
        placeholder="Enter position..."
      />
      <button type="submit">Submit</button>
    </form>
  );
}

export default ChangePosition;
