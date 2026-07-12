const classes = [
  'Cricket Bat', 'Cricket Ball', 'Football', 'Basketball', 'Volleyball',
  'Tennis Racket', 'Badminton Racket', 'Shuttlecock', 'Hockey Stick',
  'Baseball Bat', 'Baseball Glove', 'Goalkeeper Gloves', 'Helmet',
  'Golf Club', 'Sports Shoes'
];

export default function EquipmentSelect({ value, onChange }) {
  return (
    <select value={value} onChange={(event) => onChange(event.target.value)}>
      {classes.map((item) => <option key={item} value={item}>{item}</option>)}
    </select>
  );
}
