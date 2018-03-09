BEGIN TRANSACTION;

DROP TABLE PriceHistory;

CREATE TABLE PriceHistory(
Exchange text,
RelativeTimeStamp integer,
TimeStampStr text,
CurrencyCode text,
Price real
);

COMMIT;


