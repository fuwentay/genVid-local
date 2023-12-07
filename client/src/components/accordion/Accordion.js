import {useState} from 'react';

const Accordion = () => {
    // Defining setExpand and toggleExpand
    const [expand, setExpand] = useState(false);
    const toggleExpand = () => setExpand((prevExpand) => !prevExpand);

    return (
        <div>
            <button onClick={toggleExpand}>header <span>{expand ? '-': '+'}</span></button>
            {expand && <div className="content">Placeholder</div>}
        </div>
    );
};

export default Accordion;