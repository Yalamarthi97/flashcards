import React, { useState } from 'react';

import './App.css';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Button from 'react-bootstrap/Button';
import Stack from 'react-bootstrap/Stack';
import Card from 'react-bootstrap/Card';
import { getCard, saveCard, adminFetchall, adminResetAllcards, adminGetAllCorrectCards, adminGetAllFailedCards, adminFetchOneCard, createCard } from './utils/apiHandler';
import DataTable from './components/table';


function App() {

  const [haveCard, setHaveCard] = useState(false)
  const [cardData, setCardData] = useState(null)
  const [fetch, setFetchedCard] = useState(false)
  const [showdesc, setShowDesc] = useState(false)
  const [stateGetOne, setStateGetOne] = useState(false)
  const [answered, setAnswered] = useState(false)
  const [validcarddata, setValidCard] = useState(false)
  const [adminAllcards, setAdminAllcards] = useState([])
  const [allcardsBool, setAllCardsBool] = useState(false)
  const [oneState, setOneState] = useState(false)
  const [resetState, setresetState] = useState(false)
  const [successfulcards, setSuccessfulCards] = useState(false)
  const [failedcards, setfailedCards] = useState(false)
  const [fetchoneData, setFetchOneData] = useState([])
  const [val, setVal] = useState(0)
  const [guesses, setGuess] = useState(true)

  const [cardName, setCardName] = useState("")
  const [cardDesc, setCardDesc] = useState("")
  const [addCardBool, setAddcardBool] = useState(false)

  const getSuccessfulCards = () => {
    adminGetAllCorrectCards().then(res => {
      setfailedCards(true)
      console.log(res.data.message)
    }).catch(console.error)

  }
  const getFailedCards = () => {
    adminGetAllFailedCards().then(res => {
      setSuccessfulCards(true)
      console.log(res.data.message)
    }).catch(console.error)
  }

  const fetchCard = () => {
    getCard().then(res => {
      if (res.data.message === "You have no more words to review; you are permanently done!" ||
        res.data.message === "You are temporarily done; please come back later to review more words.") {
        setValidCard(false)
        setHaveCard(true)
      }
      else { setValidCard(true) }
      setCardData(res.data.message)
      setHaveCard(true)
      setFetchedCard(true)
    }).catch(console.error)

  }

  const resetAllCards = () => {
    adminResetAllcards().then(res => {
      setresetState(true)
      console.log(res.data.message)
    }).catch(console.error)
  }

  const fetchAllCards = () => {
    adminFetchall().then(res => {
      //  Reusing the same state .. 99% sure this is not the right way
      setAdminAllcards(res.data.message)
      setAllCardsBool(true)
      console.log(res.data.message)
    }).catch(console.error)

  }

  const fetchOneCard = () => {
    console.log(val)
    adminFetchOneCard(val).then(res => {

      setFetchOneData(res.data.message)
      setOneState(true)
      console.log(res.data.message)
    }).catch(console.error)
  }
  const showCardDesc = () => {
    setShowDesc(showDesc => !showDesc)
  }

  const showStateGetOne = () => {
    setStateGetOne(stateGetOne => !stateGetOne)
  }

  const answeredRight = () => {
    setAnswered(true)
    cardData && saveCard(cardData["id"], "true")
    setGuess(false)

  }

  const answeredWrong = () => {
    setAnswered(true)
    cardData && saveCard(cardData["id"], "false")
    setGuess(false)

  }

  const triggerNewCard = () => {
    setAddcardBool(true)
  }
  const createNewCard = () => {
    createCard(cardName, cardDesc)
  }


  return (
    <Container fluid>
      <div className="heading">Flashcards</div>
      <Row>
        <Stack direction="horizontal" gap={3}>
          <div className="p-2 ms-auto"><Button variant="primary" onClick={triggerNewCard}>Add Card</Button></div>
          <div className="vr" />
          <div className="p-2"><Button variant="primary" disabled={!answered} onClick={fetchCard} >Next Card</Button> </div>
        </Stack>
      </Row>
      {addCardBool && <div>
        <form onSubmit={createNewCard}>
          <label>Enter card value:
            <input
              type="text"
              value={cardName}
              onChange={(e) => setCardName(e.target.value)}
            />
          </label>
          <div style={{ "height": "5px" }}> </div>
          <label>Enter card Description:
            <input
              type="text"
              value={cardDesc}
              onChange={(e) => setCardDesc(e.target.value)}
            />
          </label>
          <div style={{ "height": "5px" }}> </div>
          <input type="submit" />
        </form>

      </div>
      }
      <Row>
        <div>
          <Button variant="success" onClick={fetchCard}>Get Card</Button>
          <Card className="text-center">
            {haveCard && validcarddata &&
              <Card.Body>

                <Card.Title>Card Value : {cardData?.["card_key"]}</Card.Title>
                <Card.Text>
                  <Button variant="primary" onClick={showCardDesc} >Show definition</Button>
                  <div style={{ "height": "15px" }}></div>
                  {showdesc &&
                    <Card.Subtitle>Description of the card : {cardData?.["card_desc"]}</Card.Subtitle>}
                </Card.Text>

                <div>
                  <Container>
                    <Row>
                      <Col md={2}></Col>
                      <Button variant="success" style={{ "padding": "15px" }} disabled={!guesses} onClick={answeredRight} >Guessed it right</Button>
                      <div style={{ "height": "10px" }}></div>
                      <Button variant="danger" style={{ "padding": "15px" }} disabled={!guesses} onClick={answeredWrong} > Wrong guess!</Button>
                      <Col md={2}></Col>
                    </Row>
                  </Container>
                </div>
              </Card.Body>
            }
            {haveCard && !validcarddata &&
              <Card.Body>
                <Card.Text>
                  {cardData}
                </Card.Text>
              </Card.Body>
            }
            {!haveCard && fetch &&
              <Card.Body>

                <Card.Title>No more cards</Card.Title>
                <Card.Text>
                  {cardData}
                </Card.Text>


              </Card.Body>}
            {!haveCard && !fetch &&
              <Card.Body>

                <Card.Title>Please fetch the card through get cards</Card.Title>



              </Card.Body>}


          </Card >
        </div>
      </Row>

      <div style={{ "height": "50px" }}></div>
      <Row>
        <Col md={5}></Col>
        <Col >Admin functions</Col>
        <Col md={5}></Col>
      </Row>
      <Row>
        <Stack direction="horizontal" gap={3}>
          <div className="p-2"><Button variant="success" onClick={fetchAllCards}>All Cards</Button></div>
          <div className="p-2"><Button variant="success" onClick={resetAllCards}>Reset all cards</Button></div>
          <div className="p-2"><Button variant="success" onClick={getSuccessfulCards}>Learnt Cards</Button></div>
          <div className="p-2"><Button variant="success" onClick={getFailedCards}>Forgotten Cards</Button></div>
        </Stack>
        {allcardsBool && <Row>

          {DataTable(adminAllcards)}
        </Row>}
        {resetState && <Row>
          Reset the entire data base, All the cards have been moved to bucket 0
        </Row>}
        {successfulcards && <Row> Table comes in here
        </Row>}

        {failedcards && <Row> Table goes here for failed cards </Row>}
      </Row>
      <Row>
        <Stack direction="horizontal" gap={3}>
          <div className="p-2"><Button variant="primary" onClick={showStateGetOne}>Get one card detail</Button></div>
          <div style={{ "height": "15px" }}></div>
          {stateGetOne &&
            <div>
              <input style={{ "alignSelf": "left" }}
                type="number"
                pattern="[0-9]*"
                value={val}
                onChange={(e) =>
                  setVal((v) => (+e.target.value))
                }
              />
              <Button variant='primary' style={{ "alignSelf": "right" }} onClick={fetchOneCard}> Submit</Button>
              {oneState && <Row>

                {DataTable(fetchoneData)}
              </Row>}
            </div>}

        </Stack>
      </Row>
    </Container>
  );
}

export default App;
