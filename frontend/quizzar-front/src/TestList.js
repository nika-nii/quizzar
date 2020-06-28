import React, { useState, useEffect } from "react";

const TestList = () => {
  const [tests, setTests] = useState([]);

  useState(() => {
    console.log("fetching...");
    fetch("http://nikanii.nikhome.net:8000/api/quiz")
      .then(res => res.json())
      .then(result => {
        setTests(result);
      });
      console.log(tests);
  });

  return (
    <div className="TestList">
      <div>вот что есть: </div>
      <ul>
        {tests.map(item => (
          <div key={item.pk}>
            {item.title} {item.description} Сложность: {item.difficulty}
          </div>
        ))}
      </ul>
    </div>
  );
};

export default TestList;
