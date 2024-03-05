# My First Web App On Rust

--- 

## Routes:

> > > GET `/plus/<number_1>/<number_2>`
>>
>> Adds two numbers
>
>> > GET `/minus/<number_1>/<number_2>`
>>
>> Subtracts second number from first number
>
>> > GET `/divide/<number_1>/<number_2>`
>>
>> Divides first number with second number
>
>> GET `/multiply/<number_1>/<number_2>`
>>
>> Multiplies two number

## How to run

1. Install [`Rust`](https://www.rust-lang.org/)
2. Clone repository
3. Run program:

```shell
cargo run
```

## Testing

Execute tests:

```shell
cargo test
```

---

### Docker

#### Build

```shell
docker build . -f Dockerfile -t <name_of_image>
```

#### Pull

```shell
docker pull ilnurha/lab2_bonus
```

#### Run

```shell
docker run -p 9000:9000 <name_of_image>
```

If you pull from `ilnurha/lab2_bonus`, name of image is "ilnurha/lab2_bonus"
