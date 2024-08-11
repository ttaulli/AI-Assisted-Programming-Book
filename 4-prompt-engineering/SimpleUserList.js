import React, { useState } from 'react';

const SimpleUserList = ({ users }) => {
  const [userList, setUserList] = useState(users);

  const removeUser = (id) => {
    setUserList(userList.filter(user => user.id !== id));
  };

  return (
    <ul>
      {userList.map(user => (
        <li key={user.id}>
          {user.name}
          <button onClick={() => removeUser(user.id)}>X</button>
        </li>
      ))}
    </ul>
  );
};

export default SimpleUserList;