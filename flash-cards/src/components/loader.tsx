// # Copied this from bootstrap

import Placeholder from 'react-bootstrap/Placeholder';

function Loader() {
    return (
        <>
            <Placeholder as="p" animation="glow">
                <Placeholder xs={12} />
            </Placeholder>
            <Placeholder as="p" animation="wave">
                <Placeholder xs={12} />
            </Placeholder>
        </>
    );
}

export default Loader;