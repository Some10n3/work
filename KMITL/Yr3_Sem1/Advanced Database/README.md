
<style>
img {
  width: 400px;
}
</style>

# Frequently Asked questions
## Midterm
- explain acid property with some exception

# Recall from last lecture
Each company car must have an employee in charge

Tx {  
&emsp;insert car row            - R1 is violated since the new car is not assigned yet <br />
&emsp;insert car assign row <br />
}

During transaction, integrity rule can be violated, R1 is deferred to after the transaction

>**Deferable** - delay the rule enforcement

# ACID properties of transaction
- Good and recommended properties of transaction
- Are properties and not definitions. (Just recommendation, it is not needed on all transactions)

## Atomicity
- Either all operations of the transaction are properly reflected in the database or none are.	
- If the operation fails during the transaction, the execution will  get rolled back automatically.
- Automicity is a good property, but it may not be suitable for a `long duration transaction`. It is the case where we don't need the ACID properties

> **A long duration transaction** is a transaction with human interventions.
```
      x
Ex. A —> B


Update T1
Set bloodgroup = ‘Z’
Where bloodgroup = ‘A’

Begin Tx
    A = A - x
    B = B + x      fails, then roll back to Begin Tx
End Tx
```

**A classic principle regarding transactions :**<br />
- *Do not use transactions in the interactive SQL mode, do it in an embeded mode.
- If you forget to commit your changes, other people who share the database are likely(many DB locks them) to be locked out until you commits
```
Set autocommit off
    update T1
    update T2
    Delete from T3
commit
```
> long duration transaction problem : 
- not suitable for `atomicity` property
- 90% work done and transaction fails
- We need to go beck to the place before the transaction failure

**Solution for `long duration transactions` :** nested Txs or Txs with eventual consistency. Means they are not committed together, but will eventually be all committed
```
Begin Tx <-- Sync point
    [        <-- Smaller sync point
    ]        <-- Smaller sync point
    [        <-- Smaller sync point
    ]        <-- Smaller sync point 
    [        <-- Smaller sync point   <-- failure happens here, rollback to end of previous sync point
    ]        <-- Smaller sync point
End Tx   <-- Sync point
```


## Consistency
- Execution of a transaction in isolation preserves the consistency of the Database

### Levels of consistency in SQL -92 (1992) or isolation levels

```
|---------T1----------| <- Sum(Acc)
    |--T2--|            <- update(Acc)
        |--T3--|        <- insert(New Acc)
```

##### Serializable 
- default, in practice is not the default
- Concurrent transactions give the same result as running them in sequence

`Sum does not see T2 and T3`

##### Repeatable read
- Only committed records can be read, repeated reads of the same record must return same value.
- However, a transaction may not be serializable 
    - It may find some records inserted by a transaction but not find others

`Sum(T1) does not see T2(update) but may see T3(insert)`

##### Read committed 
- Only committed records can be read. Successive reads may return different(but committed) values

`Sum(T1) see T2 and T3 only when they are committed`

##### Read uncommitted
- even uncommitted records can be read

`Sum(T1) see T2 and T3 even if they are uncommitted`

### ***Lowest level gives fastest response time because it has no protection at all. Only useful for approximate information(don't care about correctness)**

## Isolation
- Although multiple transactions may execute concurrently, each transaction must be unaware of other concurrently executing transactions. Intermediate transaction results must be hidden from other concurrently executed transasctions.
    - That is, for every pair of transactions Ti and Tj, it appears to Ti that either Tj finished transaction before Ti started, or Tj started execution after tj finished

```
Concurrent Tx
|------Ti------|
        |-------------Tj--------------|
Tx1
|------Ti------| |-------------Tj--------------|
Tx2
|-------------Tj--------------| |------Ti------|
```
The Concurrent Tx will only be correct if the result is the same as if we were running sequence(serial) transaction (Tx1 and Tx2). Which is tough to obtain / hard for the DBMS to handle. 
> "That is, for every pair of transactions Ti and Tj, it appears to Ti that either Tj finished transaction before Ti started, or Tj started execution after tj finished."

***Can be relaxed based on the isolation level** (but bad if low isolation level)

Some DBMS that can't handle this, will allow you to run this despite being incorrect. A lot faster but bad

```
|---------Tj----------| <- Sum(Acc)
    |--T1--|            <- update
        |--T2--|        <- insert
            |--T3--|    <- update
```
Nowadays `Isolation level` can be set to obtain desired result<br/><br/>
- Tj can see the other transactions, which is **not a good isolation principle** <br/>
- In good principle, Tj should not see T1, T2, T3
- But if we turn isolation level to highest, this design won't work because Sum transaction have to see the other transactions in order to work.

*Good transactions should have good isolation design. Nowadays design have concurrently running transactions, which is bad. Good isolation principle is hard to obtain
## Duarability
- **The only one without compromise** 
- Have to handle the system properly
- After a transaction completes successfully, the changes it has made to the database persists, even if there are system failures

# Transaction State

![./pics/TransactionStates.jpg](./pics/TransactionStates.jpg)

## Active
- The initial state; the transaction stays in this state while it is executing
## Partially Committed
- After the final statement has been executed
## Failed
- Transaction can no longer proceed
- After the discovery that normal execurion can no longer proceed
## Aborted
- or roll back
- After the transaction has been rolled back and the DB restored to its state prior to the start of the transaction.
- Two options after it has been aborted
    - restart the transaction; can be done only if no internal logical error
    - kill the transaction

## Committed
- After successful completion
- Don't confuse committed with database transfer

# Transaction recovery
## Transaction Failure
- Individual transaction failure
- **Logical errors** : Transaction cannot complete due to some internal error condition. Bad coding / bad input
- **System errors** : The DB system must terminate an active transaction due to an error condition (eg. deadlock). 

## System Crash
- Server failure
- power failure or HW failure or SW failure causes the system to crash
- **Fail-stop assumption**
    - mass storage(non-volatile storage contents) survive (not be corrupted)
    - **only lose DB buffer**
    - DB system have many integrity checks to prevent corruption of disk data

## Disk Failure
- Need people to handle this failure
- only failure that needs back up to fix
- A head crash or similar disk failure destroys all or part of disk storage
    - Destruction is assumed to be detectable : disk drives use checksums to detect failuress

## Example case
#### Transaction error [System error] (individual transaction failure)
40 unrelated SQL statements in one transaction. Involving million of rows update. Transaction 90% done overnight. Error at 5 am. The DB rolled back. 

They treated the SQL transaction as a batch file, misunderstood the definition of transaction. 

The system must keep before update version for rollback as a tempfile

The tempfile that is supposed to handle the old data is full and forced rollback.

Solution : 
- Since the 40 transactions are unrelated, you can just run them separately. So the system can recycle the tempm file.

# Storage Structure
## Volatile Storage
- Power down - lose the content

## Non-Volatile Storage
- Power down - content remains
- Survives system crash
- But may still fail, losing data

## Stable Storage
- **Mythical** form of storage that survives all failures
- not real
- Approximated by maintaining multiple copies on distinct nonvolatile media

Some DBMS implement stable storage for you
- Oracle write to several memory instead of one place (for back up)

![./pics/DataAccess.jpg](./pics/DataAccess.jpg)

- X and Y refers to DB items

- x and y are program variable

- Select X from table T2, the DBMS will look for X in the buffer. 

- If it's already there, DBMS will read from buffer to transaction work area without disk access.

- Read / Write is **within** main memory

- If not in buffer, need to load from the disk (mass storage) to memory (DB buffer)

- Input / Output handle by DBMS or Os (disk) **between** disk and main memory

Case 1 Money adding
- Transaction may commit before output

Case 2 Blood group update
- Output may take place before commmit <br/>

**Be clear of commit and output. Different**
```
Commit write on Buffer
output write on DB
```



# Problem Statements

## Problem 1
### There are committed transaction whose modified buffer values are not yet outputted to the DB space on the disk (secondary storage).
### What if failure occurs, how does those committed transaction be recovered and permanent on the DB space?

## Problem 2
### There are uncimmitted transaction whose modified buffer values already outputed to the DB space.
### If failure take place, how to cancel the modified values out of the DB space?

# Log-based Recovery

### Problem 1
- Committed transaction
- No DB modification
### Problem 2
- Uncommitted transaction
- DB modified

***Output** - Move from buffer to DB space </br>
***Database Modification** - More formal term of output </br>

### Log file
![./pics/DataAccess.jpg](./pics/log_file.png)
**Log file** keeps **log record**, which is the activities like **transaction ID**, generated at transaction start (begin transaction). The ID will be kept in the log buffer first, before moving to the log file.

**Q is the position of the data in the database. Table name, column name, primary key value .... At least 3 values in order to address these old and new values** </br></br>
**ov and nv are old and new values.** </br>

Physical commit is when the Commit record ( last line in the orange box) is saved to the log file.

Officially considered commit when it is saved to the log file

**Note that** when the data record is outputted to the logfile, the real data may still be in the DB buffer, or may already be outputted to the DB space. They are **independent**. They are **pararell processes**

### How it works : Log records
1. **<Tx, start>** : issure transaction ID
2. **<Tx, Q, ov, nv>** : in some system, they keep the row id as the Q instead of the 3 values. Only work if row ids are unique (the row id is internal and created by the sql. there's no column for id) </br>
> Q is the position of the data in the database. Table name, column name, primary key value .... At least 3 values in order to address these old and new values
3. **<Tx, commit>** : The actual commit takes place when this is output to the log file.

## Transaction Recovery Process
- **System crashes** : Maybe power failure, HW failure
- Original problem is fixed for the failure
- Restart the OS
- Restart the DBMS
- System (DBMS) knows that it is not shut down properly. It knows that failure occurs.
- Starts the recovery process
1. Recovery manager of DBMS(A module) scan the log file from the back to determine which transaction are committed or failed
2. TxID of committed transactions are kept in a list called **redo list**
TxID of failed transactions are kept in the **undo list**.
> Undo list should be smaller than redo list, since there should be only a few transactions that failed.
3. For each failed transactions in the undo list, **old values** are applied to the DB space. **Solves problem 2** Not committed but modified the DB. Use old values to cancel the transaction. </br> **Undo the modified values of uncommitted transactions**

> ![./pics/DataAccess.jpg](./pics/log_file_drawn.png)
4. For each transactions in the redo list, **new values** are applied to the DB space. **Solves problem 1** Committed but the DB stays unchanged. (not outputted from buffer yet)

### When is the content of the log file written to DB space?
- The content of the logfile are not written to the DB space on normal operations. The only time the content of the log file needsd to be written onto the DB space is during transaction recovery (number 3 and 4)
> 3. For each failed transactions in the undo list, **old values** are applied to the DB space. **Solves problem 2** Not committed but modified the DB. Use old values to cancel the transaction. </br> **Undo the modified values of uncommitted transactions**
> 4. For each transactions in the redo list, **new values** are applied to the DB space. **Solves problem 1** Committed but the DB stays unchanged. (not outputted from buffer yet)


***From the transaction POV, during normal opoeration, your transaction workspace could be somewhere on the main memory of the server, somewhere on your device. The transaction communicates directly to the DB buffer.**

### *The log file is more important than the DB space. So the log file maintenance is a must. If log file is full, and the system breaks. You simply lost the system.

## Two approaches using logs
> ![./pics/DataAccess.jpg](./pics/log_based_definition.png)
### Deferred Database Modification
- The output of DB buffer to DB space will be done **only after commit**. 
- Commit first, then defer the DB modification later to after commit
> *Defer means* postpone

> *DB modification* means output

### Immediate Database Modification
- The output may take place **before or after commit**

## Those are the definition from the book. His version doesn't separate DB recovery into two ways.

## His version is in term of log file

![./pics/DataAccess.jpg](./pics/log_file.png)

### This is a combined log, most modern DB doesn't use combined log.

**Instead, there's a separate log file that has two parts**

![./pics/DataAccess.jpg](./pics/separate_log_file.png)

## After Image Journal
- Simply keeps the new value
- Then later commits

## Before Image Journal
- Old values are in the separate file

Only one of these will be required for recovering files, so may take less space if only 1 is needed?

**He classify them into**
- only AIJ
- only BIJ
- both

### AIJ x BIJ has limited space

#### What if BIJ is full?
- The transaction which cause the problem will be rolled back

**Solution** :
- Increase the size of BIJ so that it has enough room for the records (online?)
- Bypass the BIJ? (No log) X bad don't do
- Separate the big transaction into smaller ones which commits separately **Best solution**

#### What if AIJ is full or AIJ has been extended to the media limit?
Depends on DBMS implementation
1. This is critical, the DBMS stops working
    - The DBMS consider it too risky to proceed
> If one day DBMS stops working, **first place to look is the AIJ log file**
2. The DBMS continue working at user risk

**Cheap DBMS uses option 1**

**Expensive DBMS uses option 2** </br>
    - Keep the app running at risk instead of stopping all the progress </br>
    - The system is stable enough to not crash while someone deals with the full AIJ </br>
    - **Advanced DBMS** has better solution, to have multiple AIJ to prevent the full AIJ problem. </br>
    - Ex. fires a rocket to space, 5, 4, 3, 2, AIJ full
    - Sometimes if user does not have tecnical person to operate, they won't know how to fix it and don't want it to stop working </br>

## Incremental backup using Archive Logs
- Save the AIJ log file to Archive Logs to prevent AIJ full problem
- Archive the early version of the AIJ and shrink the size of the AIJ
- DBA needs to maintain the AIJ as the size continously grows

![./pics/DataAccess.jpg](./pics/archive_log.png)

## BIJ only
- Tx commit, roll back as usual
- Both Tx recovery problem 1 and 2 are solved.
- No AIJ full problem

**How it works?**
- How to ensure phyisical commit without AIJ file?
    - Make sure that all modified buffer(changes) done by the Tx must be outputted **completely** to the DB space
    - All changes from DB buffer physically outputted to DB space(storage) is considered committed
- Consequence : **commits can be very slow** -> slow output

## AIJ only (Defer DB modification)
- defer the DB modification later to after commit
- Tx commit, roll back as usual
- Both Tx recovery problem 1 and 2 are solved.
- AIJ solves problem 1 by committing new value to log file
- **Fast commit**, very good for small Tx
- Not good with big Tx with large amt of data

**How does it solve problem 2 without BIJ?**
- The only way is to avoid the problem
- can't fix
- **Solution** : Modified DB buffer blocks are allowed to be outputted to the DB space only after Tx commits. No DB modification before commit

## Both AIJ and BIJ
- Fast commit
- Can handle big Tx with large amt of data

# Defered DB modification (AIJ only)
![./pics/DataAccess.jpg](./pics/deferred_DB_mod_1.jpg)
![./pics/DataAccess.jpg](./pics/deferred_DB_mod_2.jpg)

# Immediate DB modification (Both AIJ and BIJ)
![./pics/DataAccess.jpg](./pics/immediate_DB_mod_1.jpg)
![./pics/DataAccess.jpg](./pics/immediate_DB_mod_2.jpg)

## Log based undo redo must be idempotent
> **Idempotent** : To repeat the process several times but obtain the same result as if the process is done only once.
- In principle, redo back to the last point that buffer move to the DB space
- But the recovery manager don't know when was the last time (last point) the buffer outputs to DB space
- So it redo since the start of the log file (slow)
- Needs checkpoints

## Checkpoints
- Reference point of where the last point that DB buffer's changes are outputted to the mass storage
- Main point is to reduce recovery time when redoing
![./pics/DataAccess.jpg](./pics/checkpoints.png)
- no need to do anything(redo) with T1. Data from buffer has already been dumped to the mass storage
- only redo the part of T2 that is after the checkpoint(Tc)

# ***Log-based Recovery needs to follow a protocol called the write-ahead protocol**

> Write-ahead protocol : Log records must be outputted to the log file **before** the related modified buffer blocks are outputted ti the DB space(Mass storage)

- DBMS controls the log-based protocol
- OS outputs the logs
- So they must work together closely

### Recovery procedure of checkpointing
1. Output all log records in main memory(log buffer) onto stable storage(log file)
(according to write-ahead protocol)
2. Output all modified buffer blocks to the disk
3. Write a log record <checkpoint L> onto stable storage where L is a list of all transactions active at the time of checkpoint. (checkpoint log file)
4. All updates are stopped while doing checkpointing

![./pics/DataAccess.jpg](./pics/archive_log.png)
- There is a compulsary checkpoint at the end of each log file
- There can be many log files anywhere though

## DB back up concept
- No need back up for system crash and Tx failure
- Because we have the log files to redo and undo
- If disk crash or mass storage crash, you needs back up
- Use archive logs to backup

### Two basic kinds of back ups
### 1. Volume Backup
- Back up everything

### 2. Incremental Backup
- Only back up changes
- Eg. Only backup part of the files that is modified the past 24 hrs, or the past week. Customer wants to recover data lost that is modified on the last friday, DB admin recover it from Tuesday's backup
![./pics/DataAccess.jpg](./pics/V_I_Backup.png)
![./pics/DataAccess.jpg](./pics/DB_Crash.png)
### Rollforward Activity
Weakpoints
- May take time to rebuild DB(recover) after this crash
![./pics/DataAccess.jpg](./pics/Rollforward.png)

How to prevent
- **Cumulative backups**
> Cumulative backups : Rollforward in advance everyday
- Do the process everyday
- Every mon morning, create 2nd vol backup
- Create an offline backup copy Xday morning everyday

***A more expensive way is to use 2 phase commit**
- safer by keeping both online DB and offline DB.
- Have to commit on both DB
- Slower
- Most don't use this
- Cum backup better in overall

## Log record buffering
- log records are buffered in main memory, instead of being output directly to stable storage.
- Log records are output to stable storage when a block of log records in the buffer is full, or a log force operation is executed.
- Needs write-ahead protocal

## Database Buffering
1. Log record of block B1 must go to log file first with WAL(write ahead protocol)
2. B1 go from DB buffer to DB space
3. B2 go to DB buffer

![](./pics/DB_handling.jpg)

If you lost the log record in the log buffer, that transaction fails

### First approach :
- Log record should be outputted to log file as soon as possible to avoid <Tx, commit> losses
- If you output from log buffer to log file too ofter, io will be too busy
### Second approach : group commit
- output when a DB buffer block is full

## OS roles in buffer management
There are two approaches
![](./pics/dbms_internal.gif)
> Database System = DBMS (Author dislike term DBMS)
```
### 1. The DBMS handles DB buffer directly (raw device option)
- Reserves part of main memory to serve as buffer
- DBMS has control over reserved part rather than the OS
- Used to solve OS and DBMS compatibility problem
- size of DMBS has to be handles by DBMSadmin
- Fixed DB space size, log and DB buffer. Not flexible
- Better performance (20%)
- Good for Open systems wher OS and DBMS are not tested together (opensource / open system)
```
![](./pics/DBMS_manages.png)
![](./pics/DBMS_manages2.png)
```
### 2. The DBMS uses the virtual memory of the OS handles the buffers
- DBMS implements its buffer within VM provided by OS (OS controls)
- flexible
- DB log buffer asize can be automatically adjusted according to the DB sth(can't read his handwriting???)
- Good for Open systems wher OS and DBMS are tested together
- Imagine runnning system with opensource
```


![](./pics/DBMS_virtual.jpg)
![](./pics/DBMS_virtual_2.png)


# Scheduler

### A schedule is a sequence of execution of instructions of transactions
(execution queue)
```
Ex Tx1
update ACCT
set Amount = Amount - 50
where ACC# = 'A'
update ACCT
set Amount = Amount + 50
where ACC# = 'B'
```
![](./pics/schedule_tx.jpg)
```
Concurrent Schedule
|------Ti------|
        |-------------Tj--------------|
Serial Schedules
|------Ti------| |-------------Tj--------------|
|-------------Tj--------------| |------Ti------|
```

- We want a concurrent schedule that gives the same result as the serial one (serializable concurrent schedule)
- Not all DBMS can handle this
- Serializable means concurrent schedule, not serial schedule

Concurrent 
- serializable -> same result as the serial schedule
- not serializable -> different result as the serial schedule

**DBMS can't access some of the calculations because it's inside the application code and not the SQL code**
- So we check if it's serializability / correctness via the read and write sequence
- ignore all math operations and **only consider read and write**

![](./pics/schedule_serializable.jpg)
![](./pics/schedule_not_serializable.jpg)

### 17.6, 17.7 , 17.8 are **conflict equivalent schedules**
> shit naming, they are equivalent when swapping **non-conflict** instructions

They can be transformed into one another by the **swaps of non-conflict** instructions (work on different data items)

### 17.8 is a serial schedule
### 17.6, 17.7 , 17.8 are **conflict serializable schedule**
> **conflict serializable schedule** is the main concept of schedule. what we want. standard of correct schedule

17.6 is conflict serializable schedule because they are conflict equivalent to 17.8 serial schedule

### Conflicting Instructions
- **Definition 1** : 2 instructions conflict if they belong to different transactions, work on the same data items, and at least one operation is a write
- **Definition 2** : We say that I and J conflict if they are operations by different Tx on the same data item, and at least one of these instructions is a write operation
- (if write instruction on variable a in T1, the read before it should also be on T1. if not, there might be conflict)

> work on the same data items means accessing the same value / variable

![](./pics/Conflicting_Instructions.png)
</br></br></br></br>

## *You can set level of consistency to serializable to have **conflict serializable schedule** in SQL
- Serializable has **conflict serializable schedule** as the most common standards

![](./pics/level_of_consistency.png)



![](./pics/corr_but_no_serializable.jpg)
### not conflict serializable but gives the correct result

</br></br></br></br>
![](./pics/corr_but_no_serializable_2.jpg)


## View Serializability
- Schedule S is **view serializable** if it is view equivalent to a serial schedule
- Every conflice serializable schedule is also view serializable

> view equivalent - 


![](./pics/view_but_not_conflict.png)
#### view serializable but not conflict serializable

Conflict serializable vs View serializable

***Every view serializable that is not conflict serializable has blind writes(write without read)**

# Midterm content ends here

## Recoverable Schedule
- The source commit before the reader could commit
- Tj reads from Ti, Ti must commit before Tj commits

![](./pics/non_recoverable_schedule.jpg)
- Ti(T7) commits before Tj(T6)
- wrong, not recoverable
- T7 already read the result of T6's write. If T6 rollback to before the write, T7 will have read the wrong value


### Cascading rollback
- When T10 rollbacks, T11 and T12 must also rollback
- Should not happen, bad
- A single Tx failure, leads to a series of many Tx rollbacks
- ***It's better for T11 and T12 to just wait for the write**
![](./pics/cascading_rollbacks.jpg)

## Cascadeless Schedule
- Stronger case of recoverable schedule
- The source must commit before the reader could read
- Also recoverable


# Correct schedule = Conflict on view serializable schedules + Cascadeless schedules
- (+ no phantom phenomenons)

> Phantom Phenomenons : 

![](./pics/level_of_consistency.png)
![](./pics/loc_cascadeless.jpg)


## 4 Concurrency control problems
- 3 Concurrency control problems + phantom phenomenon
- problems to the solutions(level of consistency) stated before

1. The lost update problem
    - not conflict serializable
    - ![](./pics/lost_update_problem.jpg)
2. The uncommitted dependency problem
3. The inconsistent analysis problem
    - A is read only and is trying to calculate sth
    - B updates while A is not done calculating
    - A gets the wrong result
    - ![](./pics/Inconsistent_analysis.jpg)

***Set level of consistency of the server to serializable to prevent lost update problem and inconsistent analysis problem**



# Lock based protocols
- Slide said there are two, there are more than two. cap
- Concurrency control mechanism

## Lock based technique comprises of
1. **Lock Primitives** : Lock mechanisms
    - Exclusive lock -> read / write
    - Shared lock -> read only

2. Compatibility matrix

Discuss lock protocol after midterm

# => forgot to pull from pc

locking alone (x lock and s lock) without lock protocol does not help with 4 concurrency control problems

> Deadlock : The system is deadlocked if there's a set of Tx that every Tx in the set is waiting for other Tx

## Deadlock Prevention
- Protocols to ensure that the system will never enter the deadlock state

### 2 approaches :
### **wait-die** scheme
- non preemtive : A process will not release result before it terminate
- older Tx may wait for younger one to release data item
- younger Tx never waits for older one, they are rolled back instead

```
Tx8 has the resource
      wait          die
Tx7    ->    Tx8    <-    Tx9
```

### **wound-wait** scheme
- preemtive : A process may release result before it terminate
- older Tx wounds(force younger Tx to roll back)
- younger Tx waits for older one

```
Tx8 has the resource
      wound          wait
Tx7    ->    Tx8    <-    Tx9
```

There will be a lot of rollback so people use deadlock detection

## Deadlock Detection
- If Tx wait for too long, ask the DBMS to check in the wait for graph if there's a cyclic dependency causing a deadlock somewhere.
- If deadlock, terminate one of the Tx and make them restart
- Could set a timeout to terminate the Tx
- More popular nowadays
- Normally deadlock are checked on request (by DBA) because the system can't check all the wait for graph. System explode

## Time stamp based concurrency control
- If you don't lock, you don't get deadlock
- Instead of locking, use this instead
- Start of each Tx, Ti is issued a timestamp Ts(Ti)
- Each Tx has a unique timestamp
- 

```
Ts(Ti), Ts(Tj) = Timestamp of Tx Ti and Tj

If Ti is older than Tj
Ts(Ti) < Ts(Tj)
```

## Timestamp ordering (TSO)
- Garuntees conflict serializable without logging
  
> Q is each data item
### W-Timestamp(Q)
- Timestamp of the youngest Tx that executed write(Q) successfully

### R-Timestamp(Q)
- Timestamp of the youngest Tx that executed read(Q) successfully

### Ti can read Q if TS(Ti) younger than WTS(Q)
```
Ti wants to read Q
check TS of Ti with WTS of Q
1. If TS(Ti) < WTS(Q), means the one who wrote Q is younger than Ti. Ti needs to read the value of Q that is already overwritten, so Ti can't read and has to rollback
2. If TS(Ti) >= WTS(Q) Someone older wrote Q(Or Ti written itself if =), can read

RTS(Q) = max(RTS(Q), TS(Ti)) : If TS(Ti) younger than the old RTS, set it to the new RTS(Q)
```
### Ti can
```
Ti wants to write Q
check TS of Ti with WTS of Q
1. If TS(Ti) < RTS(Q), write too late, the younger should read from what Ti write. The younger ones already read the incorrect value, has to rollback (Value of Q that Ti is producing was needed previously, the system assumed that the value will never be produced, so Ti is rejected and gets rolled back)
2. If TS(Ti) < WTS(Q) Ti trying to write to an obsolete(Out of date) value of Q, so it gets rejected and rolled back 
3. Otherwise, the write is executed, WTS(Q) = TS(Ti)
```

- This technique also solves phantom phenomenon and inconsistent analysis
- TS protocol does not handle uncommitted dependency problem, needs to handle separately
![](./pics/TS_dep.jpg)
![](./pics/TS_EX.jpg)
***A gets rolledback**
## How to prevent A getting rolledback?
## Multiversion Scheme
![](./pics/TS_EX2.jpg)
- Write a new version of ACC3 in TXB and keep both version
- Read the correct version (The youngest version which is still older than TI)
- If B insert ACC4, A will not see ACC4

#### How far back should we keep the old version???
- We have r-1, r0, r1 .... rn. We can't keep all
- If Ti is the oldest Tx that WTS(r-n) ... WTS(r0) < Ti, delete r-n ... r-1
- Ti reads r0, delete all before r0 because Ti reads from r0
- Only keep the youngest one among the data items

## What if the DB buffer is full and can't keep r0 while rn is already made?
> r0 ... rn is kept in DB buffer

![](./pics/TS_EX3.jpg)
- Implement `BIJ` as part of DB space, so deleted r0 could be fetched back in case Ti wants to read it.

> Oracle calls DB space, Table space
> Oracle calls the BIJ space as undo table space

- Size of undo table space is significant, should be big enough

## What if the data item is so old that it gets deleted from both main mem(DB buffer) and the undo table space???
- Ti gets rolled back
> Oracle error says "Serializability can't be achieved"

## Summary
- TS protocol can avoid rollbacks in the case of inconsistency analysis and phantom phenomenon by using multiversion scheme
- Multiversion scheme : Write a new version, don't delete the old one. The Tx read the correct version. If the correct version can't be found, even in undo table, rollback the Tx.

## Timestamp protocol still can't handle uncommitted dependency problem
- TS protocol assumes that everyone commits

![](./pics/TS_dep.jpg)
- B comes before A, b update R. A tries to read R
- A can read R because B is older than A and allowed by protocol
- A reads uncommitted value (B might rollback and cause incorrect result)

## Introducing a commit bit
- There's a commit bit for each Tx
- Check the commit bit before reading
- If the commit bit says it is committed, the reader can read
- `"The reader reads only values written by a committed Tx"`
- A bit overhead for the correct result (Storing each bit and checking each Tx)

## Another solution to solve this problem
- Using locks
- x lock the uncommitted value and unlock it at the syncpoints
- Won't lead to a deadlock because with the TS protocol, only the younger reads the older ones.

![](./pics/TS_Xlock.jpg)
- Loss update problem even with the multiversion scheme
- A gets rolledback because RTS(r) is now Tb when it fetched

## To avoid rollbacks
- Some DBMS deploy 2 phase logging
- Don't get a deadlock, get a wait

# Concurrency Control techniques
1.) Strict (Rigorous) 2 phase logging with multiple granularity (+ intention locking)
- Deadlock
- `DB2`, `MS SQL Server`, `MySQL` uses these

2.) Timestamp ordering protocol + multiversion scheme + commit bits
- No locking but rollback
- Only Specialized DBMS
- `Garn faifa` use it to avoid deadlocks

## The 3rd hybrid technique :

3.) Strict(Rigorous) 2 phase locking + multiversion scheme
- Problem 1, 2 are solved by 2 phase locking
- Problem 3, 4 are solved by multiversion scheme
- `Oracle`, `PostgreSQL`, etc. uses these


# Assignment 20%
- Study concurrency control used by a relational DB DBMS and one used by a non-relational DB DBMS
- Report will be submitted after the final Exam
- 2 Person Report

### Next week will be querying and optimization

# Query Processing

![alt](./pics/quary_processing.png)

- Query the SQL
- Parser check the syntax of those words
- Translate SQL to relational Algebra
- Then `Optimizer` tries to find the best realtional algebra expression (choose the best plan)
- Optimizer has to consult DB statistic (cost based optimization from last year)
- Evaluation engine follows execution plan
- **Performance issues is at the query optimizer level**

![alt](./pics/relational_cal_alg.jpg)

## Basic steps in Query Processing
1. Parsing and translation
2. Optimization
3. Evaluation
   
![alt](./pics/RA_EX.jpg)

```
Ex1 from pic = this SQL:
select Salary
from instructor
where Salary < 75000
```
**Which one should be better in term of speed and performance the select one or the project one?**
- select first then project or project first then select
- select first better
- physical reason why it's faster, because physical structure of the database
- most DBMS keeps data by rows not by column
- each DB log reads by rows, doesn't have to read the entire DB
- Only read the ones that has salary more than 75000
- **DB for data analytics(special DB) keep data by column**

## Relational Algebra
- 8 operators
- Essential RA operators : select project and join
- Set operators : union, intersection, difference

![alt](./pics/RA_Operations.jpg)

- `select(restrict)`
  - different select than RelationalDB's select, this one is an operator
  - select tuples that satisfy given predicate
  - ![alt](./pics/select.jpg)
  - `select instructor where department name is physics`
- `Project`
  - Unary operation (only one operand (r))
  - ![alt](./pics/project1.jpg)
  - ![alt](./pics/project2.jpg)
  - `Project a1, a2, a3 from r where r is relation name
- `Join`
  - Natural join, inner join not the same
  - (RA join is equals to natural join) Matches equal value of common attributes. The common attributes appear only once at the output
  - 
    - ![alt](./pics/RA_join.jpg)
  - normal join (theta join)
    - Can change theta condition(join condition)
    > - check this out pls I didn't listen
- `Union`
  - r u s
  - In principle, you can union 2 relations (r U s) only when the relations are based on same schema (Relational Algebra)(they should have same structure), otherwise you can't union them.
  ```
  select .....
  union  .....
  select .....
  The 2 select results must be union compatible
  ```
  - Ex. char and warchar has same data length, union compatible
- `Intersection`
  - r ^ s
- `Difference(minus)`
  - r - s
  - SQL also has minus select but doesn't need to be union compatible
  ```
  select .....
  minus  .....
  select .....
  ```
- `Multiply(cartesian product)`
- `Divide`

## Divide is special, discuss next week

### Composition of RA (using them together)
![alt](./pics/compose_RA.jpg)
```
Equivalent SQL :
select name
from instructor
where departName = 'Physics'
```

### Example exercise problem
![alt](./pics/RA_EX2.jpg)
![alt](./pics/RA_EX2_ans.jpg)
- This is linear format
- Solution 2 better, because it selects the rows before joining them
- Imagine having to join big af rows, bad

### Basic principle for query optimizer : 
- Perform unary operators first to resuce number of rows binary operators has to parse
  - 30 years ago, 
- select + project, do select first

### Non linear format for RA (Execution plan)
![alt](./pics/executionn_plan1.jpg)
- full table scan at I3 and I4
- plan 2 better
- read from bottom to top

![alt](./pics/quary_processing.png)
> Then `Optimizer` tries to find the best realtional algebra expression (choose the best plan)

![alt](./pics/executionn_plan2.jpg)
- In the example, we only have a few rows and not hundreds of rows.
- The DBMS optimizer may choose to join I3 to sp directly to not mess the rows up
- In this case, number 3 is better than number 4
- **How we write SQL does not matter, the optimizer will choose for you anyway**

![alt](./pics/RA_EX3.jpg)
- subquery version of the SQL code to match the tree

## Divide operator
  - The divident(r) is a binary relation
  - The divisor(s) is a unary relation(Only one attribute)
  - the result is a unary relation whose attribute is not the attribute of the divisor and has all the matched values from the divisor
![alt](./pics/RA_divide.jpg)

## Relational Complete Language
- Must be able to query this
![alt](./pics/RA_complete.jpg)

# Selection Operation
## File scan
- Algorithm A1
  - A1(linear search)
    - when table has no index on search key(search column)
    - Cost estimate = br + 1 seek
      - br is block transfer
      - seek is a hard disk term
    - If selection on a key attribute, cost = br/2 + 1 seek
    - Can't binary search because data is not stored consecutively
    - If data is physically clustered, can binary search
      - Binary search cost estimate = upperBound(log2(br)*(tt + ts))
      - tt is transfer time
      - ts is seek time
## Index scan
- Selection using indices
- Algorithm A2, A3, A4, A5
  - A2(Clustering index, equality on key)
  - Retrieve a single record(1 row)
    - Clustering index means Tables are sorted physically
    - Search index first(from the index list on the left) then get pointer to the table
      - ![alt text](pics/A2.jpg)
    - equility on key : search and find only one tuple on row return
    - Cost estimate = (hi + 1) * (tt + ts)
      - hi is index height

  - A3(Clustering index, equality on non key)
    - Retrieve a multiple record(many rows)
    - records are on consecutive blocks (clustered)
    - Cost estimate = hi * (tt + ts) + tt + ts * b
    - b = number of blocks containing matching records
    - ![alt text](pics/A3.jpg)
    - ![alt text](pics/A3_EX.jpg)
    - ![alt text](pics/A3_EX_2.jpg)

  - A4(Secondary index, equality on key)
    - Retrieve a single record(1 row)
    - Cost estimate = (hi + n) * (tt + ts)
    - n is number of matching records not block
    - more expensive than full table scan because no cluster
    - the records are not consecutive
    - most of real life table are not clustered
      - because if update, one guy move from london to athen. have to move data from london to athen block. slow
      - just query the data faster so ppl do that
      - also when insert if overflow the block. DBMS will have to create another block for it and moving the block physically to this block will have bad performance
    - ![alt text](pics/einstein_case_A4.jpg)
    - Use A4(secondary index) because data is sorted by id number not id name and onlt 1 row(einstein only has one row)
    - Cost of finding einstein row
    - 3 nodes from index (3 until meet einstein)+ 1 node from the data each noed require seek time and transfer time

  - A5(Clustering index, comparision)
  - ![alt](./pics/A5_EX.jpg)

  - A6(Secondary index, comparision)

  - A10
    - Employ search index city
    - Employ search index status
    - union them
    - without the index from status, you need full table scan
- (more til A10, will screenshot later)

> Primary index(Clustering index) and Secondary index have nothing to do with primary, candidate key. 
> Rows have no order 'logically' But physically, they are sorted

### Search key
- attribute to set of attributes used to look up records in file
> Key is an dentifier, but a search key may not be an identifier not the same as key

## Primary Index
- Both index and dataset are sorted according to the same column(attribute)
![](./pics/primary_index.jpg)
- This is a primary index
- The arrows don't cross(Sorted according to the same column)

## Secondary Index
- non clustered index
- rows of the tables are not sorted (physically)
- In KMITL and most workplace, all indices are secondary.
  - They don't cluster the table
- Query slow
- Solution is to reorganize (cluster) the physical data
- Not easy job

# Physical datablase table organization
- keep tree space for each block, when a new row that should be in the block is inserted, will go to the tree space
- If tree space full, make a reference to an overflow block
  - overflow lock everywhere, bad perfremance
  - export db block
  - change file type
  - reorganize it (clear tree space)
  - change back and import back
  
![alt](./pics/Physical_DB_Organization.jpg)

## Cluster (in physical DB)
- Logically adjacent rows are kept adjacent physically (in the same DB block or adjacent DB)
- Clustered or sorted physically


![alt text](./pics/Cluster.jpg)
- pic1
  - Supplier table clustered by city
  - Save space by saving city name only once
  - hard to query
- pic2
  - multitable cluster
  - If you cluster by table already, can't cluster again
  
> Can we have more than one cluster (cluster by city and by )? Yes but bad performance due to having to update both physical places

![alt text](pics/ordered_indices.jpg)

#### In postgres
- create structure : get structure with primary index
- create index : get structure with secondary index

## B+ tree
- If there are K search key values in the file, the tree height is no more than upperbound(log upperbound(n/2)(k))
- Can find n(height to reach the node we are searching for) from k(size of search key)
- ![alt text](pics/BPlusTree1.jpg)
- ![alt text](pics/BPlusTree2.jpg)
- 1 node is 1 DB block

## Nested loop join


## Does choice of outer and inner loop matter?
![alt](./pics/Inner_or_Outer.jpg)
![alt](./pics/Inner_or_Outer2.jpg)
- yes
- the whole  r can be on the main mem at the same time unlike s, which is large.
- the smaller table that can fit inside the main mem at all time is faster so needs to be inside

## Block nested loop join
![alt](./pics/Block_Nested_Loop_Join.jpg)
![alt](./pics/Block_Nested_Loop_Join_EX.jpg)
- Bigger or smaller on outer loop?
  - If s outer, total = bs + (br * bs) blocks
  - If r outer, total = br + (br * bs) blocks
  - second part is constant, so it depends on first one
  - So in this algorithm, the smaller one should be on the outer loop
  - Old programmers without rule based optimizer has to know the table size and choose themselves

## Indexed nested loop join

### Database Table Physical Limit
![alt text](./pics/Database_Table_Physical_Limit.jpg)
![alt text](./pics/Database_Table_Physical_Limit_SQL.jpg)

> when sql recommend join, they show plan not run yet


# Distributed Database System
- wants to connect DB together on several machines
1. Each site(node) must be an autonomous computer
  - Autonomous : If one (computer, DB or DBMS) is disconnected, the rest can still operate
2. The sites are interconnected via computer networks
3. There are local applications that use the resources from only their local site
  - If you disconnect the computer network, the apps that is running in each machine won't fail
4. There are global applications that use resources from other sites

> 1 and 2 is a should have on every DB system
> 3 is definition of Distributed DB system (number of local apps determine Distributed DB system)
> 4 is definition of Centralized DB system (number of global apps determine Centralized DB system)

> 1-3 Distributed data processing system

![alt text](pics/Distributed_DB.png)

```
100% local application.
Bank of asia
ur account is made at ladkrabang
when withdrawing money at chiangmai
They send request to ladkrabang branch, 
deduct money locally at ladkrabang system
Then return response to chiangmai branch
So they could give you money physically
```

> Use case of distributed DB irl is when two company merges.

## Homogeneous Distributed DB
- All sites have identical schema / software
  - Everywhere should have same release and same version
  - OG definition : All sites use the same DB models
- All sites are aware of each other and agree to cooperate in processing user request
- Each site surrenders part of its autonomy in term of right to change schemas or software
  - lets other sites change database rows

## Heterogeneous Distributed DB
- Different sites may use different schema / software
  - OG definition : Different sites may use different DB models
- Sites may not be aware of each other and may provide only limited facilities for cooperation in transaction procesing

> Hard to connect if each has different DB models

> non relational DB people : Relational DB is not good for data distribution
> Not fax, we using for a long time

> Mongo DB not relational

## Distributed Data Storage
- Assume relational data models
1. Replication
  - System maintains multiple copies of data, stored in different sites, for faster retrieval and fault tolerence\
  - Good for read(local read)
  - multiple sites update, insert, delete
    - May need 2 phase commit for local / global commits
    - Eventual consistency
      - Update each site individually, eventually each site will update to have same data

2. Fragmentation
  - Relation is partitioned into several fragments stored in distinct sites
  - ex. fragment tables into bangkok customer, northern customer, southern customer. Based on same schema. When process, process each separately.

3. combined
  - relation partitioned into several fragments. System maintains several identical replicas of each fragments

### Data Replication
- A relation or fragment of a relation 

- Advantage of Replication
  - Availability - one iste is down, can use other sites
  - Paralelism - quaries on r may be processed by several nodes in pararell
  - Reduced data transfer - relation r is available locally at each site containing a replica of relation r
- Disadvantages of Replication
  - increased cost of update
  - More complex query optimizer / concurrency control

### Data Fragmentation
- Divide relation into fragments

1. Horizontal Fragmentation - Fragment relation r by rows
![alt text](pics/Horizontal_Fragmentation.jpg)
2. Vertical Fragmentation - Fragment relation r by columns
![alt text](pics/Vertical_Fragmentation.jpg)

- Advatage of fragmentation
  - Allow us to use only relavent portion of our app
  1. Horizontal
    - Allow parrallel processing on fragment of a relation
      - If you don't know which branch ur account is in. You can search in parallel on every branch
    - Allow relation to be split so that tuples are located where they are most frequently accessed
  2. Vertical
    - Allow tuples to be split so that each paty of the tuple is stored where it is most frequently accessed
    - tuple-id attribure allows efficient joining of vertical frangemts
    - allow parallel processing
  3. Mixed
    - Fragments may be successively fragmented to an arbitary depth
## Distributed DB Architecture
- app / user interacts with global DB
- Replication transparency means can see only until replication layer
- No transparency = remote procedure call, Accessing by API. Call level interface

![alt text](pics/Distributed_DB_Architecture.jpg)

![alt text](pics/Dis_DB_Arch_Transparency.jpg)
![alt text](pics/Dis_DB_Arch_Transparency_2.jpg)

```
Global Level :
Select *
From S
where status = 100
```

```
Fragments Level :
Select *
From S1
Where status = 100
Union
Select *
From S2
Where status = 100

Do all for all fragments
```

```
Location Level :
Select *
From S1 @site1
Where status = 100
Union
Select *
From S1 @site2
Where status = 100
```

### Mixed Fragmentation
![alt text](pics/Mixed_Fragmentation.jpg)
- Select employee with department <= 10 to left side(Explining the picture)

![alt text](pics/Mixed_Fragmentation_2.jpg)
- global level and fragmentation level
- select into is psuedo code. Some system has select into
- @siteX is for location level

# It's very hard to implement distributed DB from ground up. Easier to go globsal centralized DB

## Centralized 

### Distributed Transaction
- Tx may access data at several sites
- Each site has a local `Tx manager`
  - maintaining log recovery purpose
  - things we learned the whole semester
- Each site has a `Tx coordinator`
  - Start execution of Tx that originate at the site
  - Distribute sub Tx at appropriate sites for execution
  - Coordinating the termination of each Tx that originate at the site
    - To perform 2PC(2 phase commit)

### Tx system architecture
![alt text](pics/Tx_system_Arch.jpg)

#### Commit Protocol
- 2 phase commit
- 3 phase commit
- usually 2 phase because less overhead

#### 2 phase commit
  - fail-stop model : failed site simply stops working, doesn't cause any harm like sending incorrect messages
  - If a site fail, the Tx aborts
  - Execution is initiated by Tx coordinator
  - Synchronous, fail = fail together

1. Phase 1
  - Coordinator ask all participants to `prepare` to commit Tx Ti
  - Participants, upon recieving `prepare` messages, Tx manager at site determines if it can commit the Tx
    - Send `ready` out if ready to commit
![alt text](pics/Phase1.jpg)

2. Phase 2
  - T can be commited if Ci recieved `ready` T message. 
  - otherwise, T must be aborted.
  - add abortted to log
![alt text](pics/Phasee2.jpg)

### Sync Vs Async
![alt text](pics/Sync_VS_ASYNC_Distributed_DB.jpg)
- Async push
  - Ex. Primary site sends update to replicate sites in singapore, eventually will get all data
- Async Pull
  - Ex. singapore site asks for data

### Primary Sites
- Single Primary sites (fixed)
- Multiple primary sites (one at a time)
  - Ex. You have 2 sites, In the morning site A is primary site. Afternoon site B is primary site
- Simultaneous primary sites (many at a time)
  - Conflict resolution rules may choose wchich one iscorrect, maybe the least Tx id, maybe based on time, come first = right


# How Distributed DB is impractical
![alt text](pics/DBMS.png)
- Impractival
- Normlly have separate DB for each app
- Because centralized Db like this is hard to implement
- you cant dev heterogeneous distributed DB easily
- IRL ppl buy ERP

# Data Warehouse Concepts

![alt text](pics/Operational_DB_VS_Data_Warehouse.png)
![alt text](pics/intrgration.png)
- how do we know m, f is same as 0, 1? which one is male?
- encode them to make a uniform unit
- - How do we know a key A in appA represents same object A as the object A in appB with keyB?
- **Have to solve these before getiting the common Db**
  
![alt text](pics/Data_Warehouse.png)
- Morphrom is a common DB
- They use citizen ID as a uniform identifier, instead of hospital ID. 
- We don't usually update data on data warehouse
  - Could do it but not often 
- data warehouse's operations : ETL
  - Extract
  - Transfer (Transform)
  - Load
- Stable, keep past records 10 yrs, 20 yrs  
- ![alt text](pics/Data_Warehouse_2.png)

![alt text](pics/Common_Key.png)
- Make sure they have common key
![alt text](pics/Time_Value.png)
- Add time value